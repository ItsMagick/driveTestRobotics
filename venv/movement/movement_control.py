import time
import motor_control

class MovementControl:
    def __init__(self, motor: motor_control.MotorControl):
        self.motor = motor

    def move_car_left(self):
        self.motor.set_speed(0)
        self.motor.set_direction(1)
        self.motor.set_speed(-0.25)
        time.sleep(1.4)
        self.motor.set_speed(0)
        time.sleep(0.2)
        self.motor.set_speed(0.2)
        time.sleep(0.2)
        self.motor.set_speed(0)
        self.motor.set_direction(0)

    def move_car_right(self):
        self.motor.set_speed(0)
        self.motor.set_direction(-1)
        self.motor.set_speed(-0.25)
        time.sleep(1.4)
        self.motor.set_speed(0)
        time.sleep(0.2)
        self.motor.set_speed(0.2)
        time.sleep(0.2)
        self.motor.set_speed(0)
        self.motor.set_direction(0)

    def move_car_reverse(self):
        self.motor.set_speed(0)
        self.motor.set_direction(-1)
        self.motor.set_speed(-0.25)
        time.sleep(1)
        self.motor.set_direction(1)
        self.motor.set_speed(0.2)
        time.sleep(1)
        self.motor.set_speed(0)
        self.motor.set_direction(0)
