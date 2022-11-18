import time
import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

pca.frequency = 50
motor_channel = pca.channels[1]
motor_channel.duty_cycle = 0x1999

time.sleep(1)

for i in range(0x1999):
	motor_channel.duty_cycle = i
	time.sleep(0.2)
