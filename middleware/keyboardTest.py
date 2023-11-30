import keyboard
import asyncio
from basic import *

ctrl = Movement()
hands = Hands()
head = Head()

key_bindings = {
    'w': ctrl.moveForward,
    'a': ctrl.moveLeft,
    's': ctrl.moveBackward,
    'd': ctrl.moveRight,
    'space': ctrl.jump,
    'shift': ctrl.sneak,
    'r': ctrl.stop,
    'f': hands.attack,
    '[': head.rotateLeft,
    ']': head.rotateRight,
    '-': head.rotateDown,
    '=': head.rotateUp,
    'x': hands.destroyBlock,
    'c': hands.placeBlock
}

# Listen for key presses
while True:
    try:
        # Get the pressed key
        key = keyboard.read_event(suppress=True).name

        # Check if the pressed key has a corresponding function
        if key in key_bindings:
            # Execute the corresponding function
            key_bindings[key]()
    except KeyboardInterrupt:
        break
