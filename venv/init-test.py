#!/usr/bin/python3.8

import asyncio
from led import led_control
from camera import camera_detection


class MainTest(object):

    def __init__(self):
        self.ledControl = led_control.LedControl()
        self.camera_det = camera_detection.CameraDetection(None)
        self.mode = "camera"
        print('Started Dev Setup')
        futures = [self.remote_car_control()]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))
        loop.close()

    async def remote_car_control(self):
        while True:
            self.camera_det.start()

            await asyncio.sleep(0.1)


MainTest()
