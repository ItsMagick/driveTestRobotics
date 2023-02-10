import json
with open('venv/camera/roboflow_config2.json') as f:
    config = json.load(f)

    ROBOFLOW_API_KEY = config["ROBOFLOW_API_KEY"]
    ROBOFLOW_MODEL = config["ROBOFLOW_MODEL"]
    ROBOFLOW_SIZE = config["ROBOFLOW_SIZE"]

    FRAMERATE = config["FRAMERATE"]
    BUFFER = config["BUFFER"]

import cv2
import base64
import numpy as np
import requests
import time
from PIL import Image, ImageDraw, ImageFont

# Construct the Roboflow Infer URL
# (if running locally replace https://detect.roboflow.com/ with eg http://127.0.0.1:9001/)
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
url = ''.join(parts)

upload_url = "".join([
    "http://127.0.0.1:9001/",
    ROBOFLOW_MODEL,
    "?api_key=",
    ROBOFLOW_API_KEY,
    "&format=image",
    "&stroke=5"
])

# Get webcam interface via opencv-python
video = cv2.VideoCapture(0)

# Infer via the Roboflow Infer API and return the result
def infer():
    print('Stream is open: ' + str(video.isOpened()))
    # Get the current image from the webcam
    ret, img = video.read()

    # Resize (while maintaining the aspect ratio) to improve speed and save bandwidth
    height, width, channels = img.shape
    scale = ROBOFLOW_SIZE / max(height, width)
    img = cv2.resize(img, (round(scale * width), round(scale * height)))

    # Encode image to base64 string
    retval, buffer = cv2.imencode('.jpg', img)
    img_str = base64.b64encode(buffer)

    # Get prediction from Roboflow Infer API
    r = requests.post(url, data=img_str, headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "accept": "application/json"
    }, stream=True)

    print('RESPONSE: ' + str(r.content))

    preds = r.json()
    predictions = preds['predictions']

    imageHeight = preds["image"]["height"]
    imageWidth = preds["image"]["width"]
 
    test_movement(predictions, imageHeight, imageWidth)

    imgdata = base64.b64decode(img_str)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    # Parse result image
    #image = np.asarray(bytearray(resp.read()), dtype="uint8")
    #image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return img

def test_movement(predictions, imageHeight, imageWidth):
    if predictions != None:
            maxConfidence = 0
            chosenPredication = None
            for pred in predictions:
                if sortoutInvalidPersons(pred, imageHeight, imageWidth):
                    confidence = pred["confidence"]
                    x = pred["x"]
                    y = pred["y"]
                    height = pred["height"]
                    width = pred["width"]
                    if confidence > 0.6:
                        if confidence > maxConfidence:
                            maxConfidence = confidence
                            chosenPredication = pred
            if chosenPredication != None:
                print("\n--------------------")
                print("I see a person with confidence " + str(maxConfidence))
                move_for_prediction(chosenPredication["x"], chosenPredication["y"], chosenPredication["width"], chosenPredication["height"], imageWidth, imageHeight)

def move_for_prediction(x, y, width, height, frameWidth, frameHeight):
        print(x,y,width,height)
        #person detected
        #Center of person
        prozXP = x / frameWidth
        prozYP = y / frameHeight

        print("Prozentuale Pos. X: ", prozXP)
        print("Prozentuale Pos. Y: ", prozYP)

        if prozYP > 0.55:
            #Calc speed
            print("Speed: ", prozYP)

            #Calc steering
            calcSteering = (prozXP - 0.5) * 2
            print("Steering: ", calcSteering)

def sortoutInvalidPersons(predication, imageHeight, imageWidth):
        isFullWidth = imageWidth - 20 < predication["width"]
        isFullHeight = imageHeight - 20 < predication["height"]
        return not (isFullHeight and isFullWidth)

# Main loop; infers sequentially until you press "q"
while 1:
    # On "q" keypress, exit
    if(cv2.waitKey(1) == ord('q')):
        break

    # Capture start time to calculate fps
    start = time.time()

    # Synchronously get a prediction from the Roboflow Infer API
    if video.isOpened():
        image = infer()
        # And display the inference results
        cv2.imshow('image', image)

    # Print frames per second
print((1/(time.time()-start)), " fps")

# Release resources when finished
video.release()
cv2.destroyAllWindows()
