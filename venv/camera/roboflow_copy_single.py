import json
with open('venv/camera/roboflow_config.json') as f:
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
video = cv2.VideoCapture(2)

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
    detections = preds['predictions']

    imgdata = base64.b64decode(img_str)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
        image2 = Image.open(filename)

        draw = ImageDraw.Draw(image2)
        font = ImageFont.load_default()

        for box in detections:
            color = "#4892EA"
            x1 = box['x'] - box['width'] / 2
            x2 = box['x'] + box['width'] / 2
            y1 = box['y'] - box['height'] / 2
            y2 = box['y'] + box['height'] / 2

            draw.rectangle([
                x1, y1, x2, y2
            ], outline=color, width=5)

            if True:
                text = box['class']
                text_size = font.getbbox(text)

                # set button size + 10px margins
                button_size = (text_size[0] + 20, text_size[1] + 20)
                button_img = Image.new('RGBA', button_size, color)
                # put text on button with 10px margins
                button_draw = ImageDraw.Draw(button_img)
                button_draw.text((10, 10), text, font=font, fill=(255, 255, 255, 255))

                # put button on source image in position (0, 0)
                image2.paste(button_img, (int(x1), int(y1)))
        image2.show()

    # Parse result image
    #image = np.asarray(bytearray(resp.read()), dtype="uint8")
    #image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return img

# Main loop; infers sequentially until you press "q"
#while 1:
    # On "q" keypress, exit
    #if(cv2.waitKey(1) == ord('q')):
        #break

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
