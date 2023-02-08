from . import tuning
import usb.core
import usb.util
import time
from datetime import datetime, timedelta
import threading

class VoiceDetection:

    def __init__(self, movement):
        self.movement = movement

        mic = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.tuner = tuning.Tuning(mic)

        self.active = False

        self._monitor_thread = threading.Thread(target=self._run_Observer, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def start(self):
        self.active = True

    def _run_Observer(self):
        try:
            while True:
                if self.active:
                    if self.tuner.is_voice():
                        print("Is Voice")
                        print(self.tuner.direction)

                        degree = self.tuner.direction

                        if degree < 45.0 or degree > 270.0:
                            print("Is already in front of source")
                        elif 45 <= degree < 135:
                            print("Rotate left")
                            self.movement.move_car_left()
                        elif 135 <= degree < 225:
                            print("Reverse")
                            self.movement.move_car_reverse()
                        elif 225 <= degree < 270:
                            print("Rotate right")
                            self.movement.move_car_right()

                        time.sleep(5)

        except Exception as e:
            print(e)
        finally:
            self.kill()

    def kill(self):
        self.active = False
