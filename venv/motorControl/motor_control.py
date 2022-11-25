import time
import busio
from board import SCL_1, SDA_1
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit


class MovementControl:
    def __init__(self):
        self.i2c = busio.I2C(SCL_1, SDA_1)
        self.pca = PCA9685(self.i2c, address=0x40)
        self.kit = ServoKit(channels=16, i2c=self.i2c)
        self.motor = self.kit.continuous_servo[0]
        self.servo = self.kit.servo[1]
        self.setup_hardware()

    def setup_hardware(self):
        self.motor.throttle = 1
        time.sleep(1 / 10)
        self.motor.throttle = 0

    def set_direction(self, direction):
        if (direction >= -1.0) & (direction <= 1.0):
            angle = 90
            if direction < 0:
                angle = 90 + (direction * -1.0 * 50)
            if direction > 0:
                angle = 90 - (direction * 50)
            self.servo.angle = angle
            print('Set angle', angle)

    def set_speed(self, speed):
        if (speed >= -1.0) & (speed <= 1.0):
            print('Set throttle', speed)
            if speed < 0:
                self.motor.throttle = -1
                time.sleep(1/10)
                self.motor.throttle = 0
                time.sleep(1/10)
                self.motor.throttle = speed
            if speed > 0:
                self.motor.throttle = speed


