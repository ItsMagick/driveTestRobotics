import asyncio

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

        await asyncio.sleep(0)


my_movement_control = MovementControl()

print('Ready for input')
futures = [remote_car_control()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
loop.close()
