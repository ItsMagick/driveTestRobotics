import pvporcupine


porcupine = pvporcupine.create(
  access_key='${ACCESS_KEY}',
  keyword_paths=['${KEYWORD_FILE_PATH}']
)



def get_next_audio_frame():
  pass


while True:
  audio_frame = get_next_audio_frame()
  keyword_index = porcupine.process(audio_frame)
  if keyword_index == 0:
      print('detected herbie follow me')
      
