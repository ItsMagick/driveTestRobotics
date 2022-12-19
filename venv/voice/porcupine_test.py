import pvporcupine


porcupine = pvporcupine.create(
  access_key='nzah8bgrstj0FbW+BTI7qeGM1qF3MTi+jmqtHfn69Q+gT7MKoxgRfg==',
  keyword_paths=['venv/voice/Herbie-follow-me_en_jetson_v2_1_0.ppn']
)

def get_next_audio_frame():
  pass


while True:
  audio_frame = get_next_audio_frame()
  keyword_index = porcupine.process(audio_frame)
  if keyword_index == 0:
      print('detected herbie follow me')

