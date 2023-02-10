import time

class MovementControl(object):
    def __init__(self, motor):
        self.motor = motor

    def move_car_left(self, voice_angle):
        self.motor.set_speed(0)
        self.motor.set_direction(1)
        self.motor.set_speed(-0.8)
        sleep_time = (voice_angle / 150) + 0.4
        time.sleep(sleep_time)
        self.motor.set_speed(0)
        self.motor.set_direction(0)
        time.sleep(0.2)
        self.motor.set_speed(0.6)
        time.sleep(0.2)
        self.motor.set_speed(0)
        self.motor.set_direction(0)

    def move_car_right(self, voice_angle):
        self.motor.set_speed(0)
        self.motor.set_direction(-1)
        self.motor.set_speed(-0.8)
        time.sleep(1.4)
        self.motor.set_speed(0)
        self.motor.set_direction(0)
        time.sleep(0.2)
        self.motor.set_speed(0.6)
        time.sleep(0.2)
        self.motor.set_speed(0)
        self.motor.set_direction(0)

    def move_car_reverse(self):
        self.motor.set_speed(0)
        self.motor.set_direction(-1)
        self.motor.set_speed(-0.8)
        time.sleep(1.2)
        self.motor.set_direction(1)
        self.motor.set_speed(0.6)
        time.sleep(1.2)
        self.motor.set_speed(0)
        self.motor.set_direction(0)
