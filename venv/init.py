import asyncio
import time
import os

from motorControl import motor_control
from controller import xinput_controller


class Main:

    def __init__(self):
        self.moveControl = motor_control.MovementControl()
        self.controller = xinput_controller.XboxController()
        self.mode = "stop"
        print('Ready for input')
        futures = [self.remote_car_control()]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))
        loop.close()

    async def remote_car_control(self):
        while True:
            if self.controller.B == 1:
                self.mode = "stop"
            if self.controller.A == 1:
                self.mode = "voice"
            if self.controller.Y == 1:
                self.mode = "controller"
            if self.controller.Back == 1:
                self.mode = "shutdown"

            print("Mode:" + self.mode)

            if self.mode == "shutdown":
                os.system("sudo shutdown now -h")

            if self.mode == "stop":
                self.moveControl.set_speed(0)

            if self.mode == "controller":
                self.controller_observer()

            # key_observer()

            await asyncio.sleep(0.1)

    def controller_observer(self):
        self.moveControl.set_speed(self.controller.RightTrigger / 2)
        self.moveControl.set_direction(self.controller.LeftJoystickX)

    async def key_observer(self):
        key = input()

        if key == 'w':
            print('forward')
            self.moveControl.set_direction(0)
        if key == 'a':
            print('left')
            self.moveControl.set_direction(-1)
        if key == 'd':
            print('right')
            self.moveControl.set_direction(1)

        if key == 'dir':
            print('Enter direction from -1 to 1')
            self.moveControl.set_direction(float(input()))

        if key == 'speed':
            print('Enter Speed level from -1 to 1')
            speed = float(input())
            print('Enter duration in seconds as float')
            duration = float(input())

            self.moveControl.set_speed(speed)
            time.sleep(duration)
            self.moveControl.set_speed(0)


Main()
