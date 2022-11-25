import asyncio
import time

from motor_control import MovementControl


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

        try:
            if int(key) is not None:
                print('Speed for seconds ', int(key))
                my_movement_control.set_speed(0.3)
                time.sleep(0.5*int(key))
                my_movement_control.set_speed(0)
        finally:
            await asyncio.sleep(0)



my_movement_control = MovementControl()

print('Ready for input')
futures = [remote_car_control()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
loop.close()
