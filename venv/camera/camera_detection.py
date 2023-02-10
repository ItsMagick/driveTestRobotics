import json

with open('/home/herbie/Documents/driveTestRobotics/venv/camera/roboflow_config.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = config["ROBOFLOW_SIZE"]

    FRAMERATE = config["FRAMERATE"]
    BUFFER = config["BUFFER"]

import cv2
import math
import base64
import requests
import threading
class CameraDetection(object):

    def __init__(self, movement, motor):
        self.movement = movement
        self.motor = motor

        self.active = False

        self.url = None
        self.upload_url = None
        self.define_urls()
        self.video = cv2.VideoCapture(2) #Attention: This index need adjustments, based on the current connected cameras
        
    def start(self):
        self.active = True

    def on_thread_call(self):
        try:
            if self.active:
                if self.video.isOpened():
                    snapshot = self.snapshot()
                    self.handle_snapshot(snapshot)

        except Exception as e:
            print(e)

    def kill(self):
        self.active = False

    def define_urls(self):
        parts = []
        url_base = 'http://127.0.0.1:9001/'
        endpoint = ROBOFLOW_MODEL
        access_token = '?api_key='+ROBOFLOW_API_KEY
        format = '&format=json'
        confidence = '&confidence=10'
        stroke='&stroke=5'
        parts.append(url_base)
        parts.append(endpoint)
        parts.append(access_token)
        parts.append(format)
        parts.append(confidence)
        parts.append(stroke)
        self.url = ''.join(parts)

        self.upload_url = "".join([
            "http://127.0.0.1:9001/",
            ROBOFLOW_MODEL,
            "?api_key=",
            ROBOFLOW_API_KEY,
            "&format=image",
            "&stroke=5"
        ])

    def sortoutInvalidPersons(self, predication, imageHeight, imageWidth):
        isFullWidth = imageWidth - 20 < predication["width"]
        isFullHeight = imageHeight - 20 < predication["height"]
        return not (isFullHeight and isFullWidth)


    def snapshot(self):
        # Get the current image from the webcam
        ret, img = self.video.read()

        # Resize (while maintaining the aspect ratio) to improve speed and save bandwidth
        height, width, channels = img.shape
        scale = ROBOFLOW_SIZE / max(height, width)
        img = cv2.resize(img, (round(scale * width), round(scale * height)))

        # Encode image to base64 string
        retval, buffer = cv2.imencode('.jpg', img)
        img_str = base64.b64encode(buffer)

        # Get prediction from Roboflow Infer API
        r = requests.post(self.url, data=img_str, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json"
        }, stream=True)

        return r

    def handle_snapshot(self, snapshot):
        obj = snapshot.json()
        predictions = obj["predictions"]
        imageHeight = obj["image"]["height"]
        imageWidth = obj["image"]["width"]
        if predictions != None:
            maxConfidence = 0
            chosenPredication = None
            for pred in predictions:
                if self.sortoutInvalidPersons(pred, imageHeight, imageWidth):
                    confidence = pred["confidence"]
                    x = pred["x"]
                    y = pred["y"]
                    height = pred["height"]
                    width = pred["width"]
                    if confidence > 0.8:
                        if confidence > maxConfidence:
                            maxConfidence = confidence
                            chosenPredication = pred
            if chosenPredication != None:
                print("--------------------")
                print("I see a person with confidence " + str(maxConfidence))
                self.move_for_prediction(chosenPredication["x"], chosenPredication["y"], chosenPredication["width"], chosenPredication["height"], imageWidth, imageHeight)
            else: self.move_stay()
        else: self.move_stay()

    def move_for_prediction(self, x, y, width, height, frameWidth, frameHeight):
        print(x,y,width,height)
        #person detected
        #Center of person
        prozXP = x / frameWidth
        prozYP = y / frameHeight

        print("Prozentuale Pos. X: ", prozXP)
        print("Prozentuale Pos. Y: ", prozYP)

        if prozYP <= 0.55:
            self.motor.set_speed(0)
        else:
            #Calc speed
            print("Speed: ", prozYP)
            self.motor.set_speed(prozYP)

            #Calc steering
            calcSteering = math.tanh((prozXP * 2.0) - 1.0) * 0.25
            print("Raw-Steering: ", calcSteering)
            if calcSteering > 1.0:
                calcSteering = 1.0
            if calcSteering < -1.0:
                calcSteering = -1.0
            print("Steering: ", calcSteering)
            self.motor.set_direction(calcSteering)
            
    def move_stay(self):
        self.motor.set_speed(0)
