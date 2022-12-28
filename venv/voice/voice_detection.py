from . import tuning
import usb.core
import usb.util
import time
import wave
import os
import argparse
import struct
from datetime import datetime, timedelta
import threading
import sounddevice as sd
import wavio as wv

class VoiceDetection:
    temp_file_name = "/home/herbie/Desktop/test.wav"
    current = None
    def __init__(self):
        self.wav_file = None
        mic = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.tuner = tuning.Tuning(mic)
        
        self.active = False

        self._monitor_thread = threading.Thread(target=self._run_Observer, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

        self.recorder = None

    def start(self):
        self.active = True

    def _run_Observer(self):
        try:
            while True:
                if self.active:
                    print("In Pipe")
                    if self.tuner.is_voice():
                        print("Is Voice")
                        if self.current is None:
                            print("Start Recording")
                            self.start_recording()
                        self.current = datetime.now()

                    if self.current is not None:
                        if datetime.now() > (self.current + timedelta(seconds=1)):
                            print("Kill to write")
                            self.kill()
                            wv.write("/home/herbie/Desktop/test_" + str(time.time()) + ".wav", self.recorder, 44100, sampwidth=2)

                            print("Recorded Snippet")
                            #TODO: Analyse
        except Exception as e:
            print(e)

        finally:
            self.kill()
            

    def start_recording(self):
        #if os.path.exists(self.temp_file_name):
            #os.remove(self.temp_file_name)

        print("Begin to record")
        self.recorder = sd.rec(int(6 * 44100),
                           samplerate=44100, channels=2)
        print("Is Recording")

    def kill(self):
        sd.stop()
        self.current = None
        self.active = False
