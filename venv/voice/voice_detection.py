from . import tuning
import usb.core
import usb.util
import time
import wave
import os
import argparse
import struct
from datetime import *
from threading import Thread
import pvporcupine
from pvrecorder import PvRecorder

class VoiceDetection:
    temp_file_name = "./temp.wav"
    current = None
    def __init__(self):
        self.wav_file = None
        mic = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.tuner = tuning.Tuning(mic)

        self.porcupine = pvporcupine.create(
            access_key='nzah8bgrstj0FbW+BTI7qeGM1qF3MTi+jmqtHfn69Q+gT7MKoxgRfg==',
        )
        self.recorder = None

    def start(self):
        print("Frame Length:", self.porcupine.frame_length)
        self.recorder = PvRecorder(device_index=0, frame_length=self.porcupine.frame_length)
        self.recorder.start()

    def runObserver(self):
        while True:
            try:
                if self.tuner.is_voice():
                    if self.current is None:
                        self.startRecording()
                    self.current = datetime.now()

                if datetime.now() > (self.current + timedelta(seconds=1)):
                    self.wav_file.close()
                    print("Recorded Snippet")
                    #TODO: Analyse
                else:
                    pcm = self.recorder.read()
                    if self.wav_file is not None:
                        self.wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))

            finally:
                self.kill()
    def startRecording(self):
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

        self.wav_file = wave.open(self.temp_file_name, "w")
        self.wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))

    def kill(self):
        if self.recorder is not None:
            self.recorder.delete()

        if self.wav_file is not None:
            self.wav_file.close()


