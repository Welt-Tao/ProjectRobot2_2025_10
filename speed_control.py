from microbit import display, Image, sleep
import tinybit

display.show(Image.HAPPY)
SPEED_PROFILES = [
    (0, 0, 1000),
    (50, 50, 1000),
    (100, 100, 1000),  # Slow
    (150, 150, 1000),  # Medium
    (200, 200, 1000),  # Fast
    (255, 255, 1000),  # Full speed
]

while True:
    for left_speed, right_speed, duration in SPEED_PROFILES:
        tinybit.car_run(left_speed, right_speed)
        sleep(duration)  # Wait for specified duration
