import asyncio
import time

from motorControl import MovementControl


async def remote_car_control():
    while True:
        key = input()

        if key == 'w':
            print('forward')
            my_movement_control.set_direction(0)
        if key == 'a':
            print('left')
            my_movement_control.set_direction(-1)
        if key == 'd':
            print('right')
            my_movement_control.set_direction(1)

        if key == 'dir':
            print('Enter direction from -1 to 1')
            my_movement_control.set_direction(float(input()))

        if key == 'speed':
            print('Enter Speed level from -1 to 1')
            speed = float(input())
            print('Enter duration in seconds as float')
            duration = float(input())

            my_movement_control.set_speed(speed)
            time.sleep(duration)
            my_movement_control.set_speed(0)

        await asyncio.sleep(0)


my_movement_control = MovementControl()

print('Ready for input')
futures = [remote_car_control()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
loop.close()
