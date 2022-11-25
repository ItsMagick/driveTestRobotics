import time
import busio
from board import SCL_1, SDA_1
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit

i2c = busio.I2C(SCL_1, SDA_1)
pca = PCA9685(i2c, address=0x40)

kit = ServoKit(channels=16, i2c=i2c)

motor = kit.continuous_servo[0]
servo = kit.servo[1]

motor.throttle = 1
time.sleep(1/10)
motor.throttle = 0

motor.throttle = 0.2
time.sleep(2)
motor.throttle = 0

servo.angle = 90
time.sleep(1/10)
servo.angle = 40
time.sleep(5)
servo.angle = 130
time.sleep(5)
servo.angle = 90
