import tuning
import usb.core
import usb.util
import time
import wave
import os
import argparse
import struct
from datetime import datetime
from threading import Thread
import pvporcupine
from pvrecorder import PvRecorder

class VoiceDetection:
    temp_file_name = "./temp.wav"
    current = None
    def __init__(self):
        self.wav_file = None
        mic = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.tuner = tuning.Tuning(dev)
        self.recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
        self.recorder.start()

    def runObserver(self):
        while True:
            try:
                if self.tuner.is_voice():
                    if self.current is None:
                        self.startRecording()
                        self.current = datetime.now()


                    pcm = self.recorder.read()
                    self.wav_file.writeframes(struct.pack("h" * len(pcm), *pcm))
            finally:
                if self.recorder is not None:
                    self.recorder.delete()

                if self.wav_file is not None:
                    self.wav_file.close()
    def startRecording(self):
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

        self.wav_file = wave.open(self.temp_file_name, "w")
        self.wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))

