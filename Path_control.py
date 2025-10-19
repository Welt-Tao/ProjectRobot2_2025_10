from microbit import sleep, display, Image, button_a, button_b
import tinybit

# Custom letter images
LETTER_IMAGES = {
    "L": Image("90000:90000:90000:90000:99999"),
    "O": Image("09990:90009:90009:90009:09990"),
    "D": Image("99000:90900:90090:90009:99999"),
    "Z": Image("99999:00090:00900:09000:99999"),
}
# Movement sequences for each letter
LETTER_MOVEMENTS = {
    "L": [("run", 80, 1000), ("spinleft", 180, 400), ("run", 80, 1000), ("stop", 0, 0)],
    "O": [
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("stop", 0, 0),
    ],
    "D": [
        ("run", 80, 1000),
        ("spinleft", 180, 500),
        ("run", 80, 1500),
        ("spinleft", 80, 1000),
        ("run", 80, 1200),
        ("stop", 0, 0),
    ],
    "Z": [
        ("run", 80, 1000),
        ("spinright", 120, 500),
        ("run", 80, 1300),
        ("spinleft", 65, 600),
        ("run", 60, 1300),
        ("stop", 0, 0),
    ],
}
# Initialize
display.show(Image.HAPPY)
current_letter = 0
letter_keys = list(LETTER_IMAGES.keys())
execute_flag = False


def execute_movement_sequence(letter):
    """Execute the movement sequence for a given letter"""
    display.show(LETTER_IMAGES[letter])
    sleep(1000)  # Show the letter before moving
    for action, speed, duration in LETTER_MOVEMENTS[letter]:
        if action == "run":
            tinybit.car_run(speed)
        elif action == "spinleft":
            tinybit.car_spinleft(speed)
        elif action == "spinright":
            tinybit.car_spinright(speed)
        elif action == "stop":
            tinybit.car_stop()
        if duration > 0:
            sleep(duration)


while True:
    # Button A cycles through letters
    if button_a.was_pressed():
        current_letter = (current_letter + 1) % len(letter_keys)
        display.show(LETTER_IMAGES[letter_keys[current_letter]])
    # Button B executes the current letter movement
    if button_b.was_pressed():
        execute_flag = True
    if execute_flag:
        execute_movement_sequence(letter_keys[current_letter])
        execute_flag = False
        display.clear()
        sleep(1000)
        display.show(LETTER_IMAGES[letter_keys[current_letter]])
