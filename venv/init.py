#!/usr/bin/python3.8

import asyncio
import time
import os
import logging
import threading

from controller import xbox_controller
from led import led_control
from movement import movement_control
from movement import motor_control
from voice import voice_detection
from camera import camera_detection


class Main(object):

    def __init__(self):
        # Unscheduled modules
        self.motor = motor_control.MotorControl()
        self.movement = movement_control.MovementControl(self.motor)
        self.ledControl = led_control.LedControl()

        # Scheduled modules
        self.controller = xbox_controller.XboxController()
        self.voice_det = voice_detection.VoiceDetection(self.movement)
        self.camera_det = camera_detection.CameraDetection(self.movement, self.motor)

        self._monitor_thread = threading.Thread(target=self.threadObserver, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

        self.mode = "stop"
        self.ledControl.set_red()
        print('Ready for input')
        futures = [self.remote_car_control()]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))
        loop.close()

    async def remote_car_control(self):
        while True:
            if self.controller.B == 1:
                self.mode = "stop"
                self.ledControl.set_red()
            if self.controller.X == 1:
                self.mode = "voice"
                self.ledControl.set_voice()
            if self.controller.Y == 1:
                self.mode = "controller"
                self.ledControl.set_yellow()
            if self.controller.A == 1:
                self.mode = "camera"
                self.ledControl.set_green()

            if self.mode == "stop":
                self.motor.set_speed(0)
                if self.controller.Back == 1:
                    self.mode = "shutdown"
                if self.controller.Start == 1:
                    os.system("systemctl restart herbieStartup.service")

            if self.mode == "shutdown":
                os.system("shutdown now")

            if self.mode == "voice":
                self.voice_det.start()
            else:
                self.voice_det.kill()

            if self.mode == "camera":
                self.camera_det.start()
            else:
                self.camera_det.kill()

            if self.mode == "controller":
                self.controller_observer()
                if self.controller.RightJoystickX < -0.9:
                    self.movement.move_car_left()
                if self.controller.RightJoystickX > 0.9:
                    self.movement.move_car_right()
                if self.controller.RightJoystickY < -0.9:
                    self.movement.move_car_reverse()

            # key_observer()

            await asyncio.sleep(0.1)

    def threadObserver(self):
        while True:
            self.voice_det.on_thread_call()
            self.camera_det.on_thread_call()


    def controller_observer(self):
        if self.controller.LeftTrigger > 0:
            self.motor.set_speed(-self.controller.LeftTrigger)
        elif self.controller.RightTrigger > 0:
            self.motor.set_speed(self.controller.RightTrigger)
        else:
            self.motor.set_speed(0)
        self.motor.set_direction(self.controller.LeftJoystickX)

    async def key_observer(self):
        key = input()

        if key == 'w':
            print('forward')
            self.motor.set_direction(0)
        if key == 'a':
            print('left')
            self.motor.set_direction(-1)
        if key == 'd':
            print('right')
            self.motor.set_direction(1)

        if key == 'dir':
            print('Enter direction from -1 to 1')
            self.motor.set_direction(float(input()))

        if key == 'speed':
            print('Enter Speed level from -1 to 1')
            speed = float(input())
            print('Enter duration in seconds as float')
            duration = float(input())

            self.motor.set_speed(speed)
            time.sleep(duration)
            self.motor.set_speed(0)


Main()
