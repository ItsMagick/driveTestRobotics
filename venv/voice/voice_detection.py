from . import tuning
import usb.core
import usb.util
import time
from datetime import datetime, timedelta
import threading

class VoiceDetection(object):

    def __init__(self, movement):
        self.movement = movement

        mic = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.tuner = tuning.Tuning(mic)

        self.active = False

    def start(self):
        self.active = True

    def on_thread_call(self):
        try:
            if self.active:
                if self.tuner.is_voice():
                    print("Is Voice")
                    print(self.tuner.direction)

                    degree = self.tuner.direction

                    if degree < 30.0 or degree > 330.0:
                        print("Is already in front of source")
                    elif 30 <= degree < 135:
                        print("Rotate left")
                        self.movement.move_car_left()
                    elif 135 <= degree < 225:
                        print("Reverse")
                        self.movement.move_car_reverse()
                    elif 225 <= degree < 330:
                        print("Rotate right")
                        self.movement.move_car_right()

                    return True
        except Exception as e:
            print(e)

    def kill(self):
        self.active = False
