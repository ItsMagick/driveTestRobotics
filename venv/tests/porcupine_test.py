import argparse
import os
import struct
import wave
from datetime import datetime
from threading import Thread

import pvporcupine
from pvrecorder import PvRecorder

class PorcupineRecording:
  
  def run(self):
    porcupine = None
    recorder = None
    wav_file = None
    try:
        porcupine = pvporcupine.create(
          access_key='nzah8bgrstj0FbW+BTI7qeGM1qF3MTi+jmqtHfn69Q+gT7MKoxgRfg==',
          keyword_paths=['venv/voice/Herbie-follow-me_en_jetson_v2_1_0.ppn']
        )

        recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
        recorder.start()

        if self._output_path is not None:
            wav_file = wave.open(self._output_path, "w")
            wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))

        print('Using device: %s', recorder.selected_device)


        while True:
            pcm = recorder.read()

            result = porcupine.process(pcm)
            if result >= 0:
                print('[%s] Detected %s' % (str(datetime.now())))
    except pvporcupine.PorcupineInvalidArgumentError as e:
        print("One or more arguments provided to Porcupine is invalid: ")
        print("If all other arguments seem valid, ensure that '%s' is a valid AccessKey")
        raise e
    except pvporcupine.PorcupineActivationError as e:
        print("AccessKey activation error")
        raise e
    except pvporcupine.PorcupineActivationLimitError as e:
        print("AccessKey '%s' has reached it's temporary device limit")
        raise e
    except pvporcupine.PorcupineActivationRefusedError as e:
        print("AccessKey '%s' refused")
        raise e
    except pvporcupine.PorcupineActivationThrottledError as e:
        print("AccessKey '%s' has been throttled")
        raise e
    except pvporcupine.PorcupineError as e:
        print("Failed to initialize Porcupine")
        raise e
    except KeyboardInterrupt:
        print('Stopping ...')
    finally:
        if porcupine is not None:
            porcupine.delete()

        if recorder is not None:
            recorder.delete()

        if wav_file is not None:
            wav_file.close()

  def show_audio_devices(self):
      devices = PvRecorder.get_audio_devices()

      for i in range(len(devices)):
          print('index: %d, device name: %s' % (i, devices[i]))


