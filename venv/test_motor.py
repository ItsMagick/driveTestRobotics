import RPi.GPIO as GPIO
import time

output_pin = 33

GPIO.setmode(GPIO.BOARD)
p = GPIO.PWM(output_pin, 50)
val = 25
incr = 5
p.start(val)

try:
 while True:
  time.sleep(0.25)
  if val >= 100:
   incr
