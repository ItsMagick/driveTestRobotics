import json
with open('/home/herbie/Documents/driveTestRobotics/venv/camera/roboflow_config.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = config["ROBOFLOW_SIZE"]

    FRAMERATE = config["FRAMERATE"]
    BUFFER = config["BUFFER"]

import cv2
import base64
import requests
import threading
class CameraDetection(object):

    def __init__(self, movement):
        self.movement = movement

        self.active = False

        self._monitor_thread = threading.Thread(target=self._run_Observer, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

        self.url = None
        self.upload_url = None
        self.define_urls()
        self.video = cv2.VideoCapture(2) #Attention: This index need adjustments, based on the current connected cameras

    def start(self):
        self.active = True

    def _run_Observer(self):
        try:
            while True:
                if self.active:
                    if self.video.isOpened():
                        snapshot = self.snapshot()
                        self.handle_snapshot(snapshot)

        except Exception as e:
            print(e)
        finally:
            self.kill()

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
            for pred in predictions:
                confidence = pred["confidence"]
                x = pred["x"]
                y = pred["y"]
                height = pred["height"]
                width = pred["width"]
                if confidence > 0.6:
                    print("I see a person with confidence " + str(confidence))
                    self.move_for_prediction(x, y, width, height)

    def move_for_prediction(self, x, y, width, height):
        print(x,y,width,height)
        

