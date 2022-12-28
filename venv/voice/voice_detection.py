import tuning
import usb.core
import usb.util
import time
import wave
import os
import argparse
import struct
from datetime import *
from threading import Thread
import sounddevice as sd
import wavio as wv

class VoiceDetection:
    temp_file_name = "./temp.wav"
    current = None
    def __init__(self):
        self.wav_file = None
        mic = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.tuner = tuning.Tuning(mic)

        self.recorder = None

    def run_Observer(self):
        while True:
            try:
                if self.tuner.is_voice():
                    if self.current is None:
                        self.start_recording()
                    self.current = datetime.now()

                if datetime.now() > (self.current + timedelta(seconds=1)):
                    self.kill()
                    wv.write(self.temp_file_name, self.recorder, 44100, sampwidth=2)

                    print("Recorded Snippet")
                    #TODO: Analyse

            finally:
                self.kill()

    def start_recording(self):
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

        self.recorder = sd.rec(int(6 * 44100),
                           samplerate=44100, channels=2)

    def kill(self):
        sd.stop()
        self.current = None
