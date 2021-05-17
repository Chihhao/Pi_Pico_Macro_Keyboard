import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button_pins = [board.GP7, board.GP8, board.GP9,
				board.GP10, board.GP11, board.GP12,
				board.GP13, board.GP14, board.GP15]

button_mapping = [
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.ONE],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.TWO],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.THREE],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.FOUR],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.FIVE],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.SIX],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.SEVEN],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.EIGHT],
    [Keycode.RIGHT_CONTROL, Keycode.RIGHT_ALT, Keycode.NINE]]

keyboard = Keyboard(usb_hid.devices)
buttons = [digitalio.DigitalInOut(bp) for bp in button_pins]

for btn in buttons:
	btn.direction = digitalio.Direction.INPUT
	btn.pull = digitalio.Pull.UP

while True:
	last_pressed = [False for _ in button_pins]
	
	for ix, btn in enumerate(buttons):
		if not btn.value: last_pressed[ix] = True

	
	for ix, pressed in enumerate(last_pressed):
		if pressed:
			keyboard.press(*button_mapping[ix])
			time.sleep(0.01)
			keyboard.release(*button_mapping[ix])
			time.sleep(0.25)

	time.sleep(0.001)
		
	