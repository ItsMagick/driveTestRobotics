import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
#motorKit = MotorKit(i2c=board.I2C())

#pwm.setPWMFreq(50)
#pwm.setPWM(1, 0, 400)

#kit.servo[0].angle = 90
#kit.servo[0].angle = 44
kit.continuous_servo[1].set_pulse_width_range(1, 2)
kit.continuous_servo[1].throttle = 1
time.sleep(1)
kit.continuous_servo[1].throttle = -1
time.sleep(1)
#kit.servo[0].angle = 30
#time.sleep(1)
#kit.servo[0].angle = 120
#time.sleep(1)
#kit.servo[0].angle = 90
#kit.continuous_servo[1].throttle = 0

#motorKit.motor1.throttle = 1
#time.sleep(2)
#motorKit.motor1.throttle = None
