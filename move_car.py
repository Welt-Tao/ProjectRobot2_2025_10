import tinybit
from microbit import display, Image, sleep

display.show(Image.ARROW_S)
tinybit.car_run(150)
sleep(2000)
tinybit.car_stop()
