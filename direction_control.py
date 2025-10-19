from microbit import display, Image, sleep
import tinybit

MOVEMENTS = [
    (tinybit.car_run, 150, Image.ARROW_S, 1000),
    (tinybit.car_back, 150, Image.ARROW_N, 1000),
    (tinybit.car_left, 150, Image.ARROW_E, 1000),
    (tinybit.car_right, 150, Image.ARROW_W, 1000),
    (tinybit.car_spinleft, 150, Image.ARROW_E, 1000),  # Spin left
    (tinybit.car_spinright, 150, Image.ARROW_W, 1000),  # Spin right
]
while True:
    for move_func, speed, arrow, duration in MOVEMENTS:
        move_func(speed)
        display.show(arrow)
        sleep(duration)
    tinybit.car_stop()
    display.clear()
    sleep(1000)
