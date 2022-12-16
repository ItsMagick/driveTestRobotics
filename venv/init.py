import asyncio
import time

from motorControl import motor_control
from controller import xinput_controller


async def remote_car_control():
    while True:
        controllerObserver()
        #keyObserver()

        await asyncio.sleep(0.1)

def controllerObserver():
    moveControl.set_speed(controller.RightTrigger / 2)
    moveControl.set_direction(controller.LeftJoystickX)

async def keyObserver():
    key = input()
    
    if key == 'w':
        print('forward')
        moveControl.set_direction(0)
    if key == 'a':
        print('left')
        moveControl.set_direction(-1)
    if key == 'd':
        print('right')
        moveControl.set_direction(1)

    if key == 'dir':
        print('Enter direction from -1 to 1')
        moveControl.set_direction(float(input()))

    if key == 'speed':
        print('Enter Speed level from -1 to 1')
        speed = float(input())
        print('Enter duration in seconds as float')
        duration = float(input())

        moveControl.set_speed(speed)
        time.sleep(duration)
        moveControl.set_speed(0)



moveControl = motor_control.MovementControl()
controller = xinput_controller.XboxController()

print('Ready for input')
futures = [remote_car_control()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
loop.close()
