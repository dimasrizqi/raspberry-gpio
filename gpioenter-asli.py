import uinput
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  #GPIO.BCM uses the GPIO port name for reference

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

device = uinput.Device([uinput.KEY_ENTER])

# Boolean to keep track of the button
Enter = False

while True:
    if (not Enter) and (not GPIO.input(26)):      # Big Red Button pressed
       Enter = True
       device.emit(uinput.KEY_ENTER, 1)       # press ENTER keyboard button
    if Enter and GPIO.input(26):                      # Big Red Button released
       Enter = False
       device.emit(uinput.KEY_ENTER, 0)       # ENTER keyboard button released
    time.sleep(0.1)                                           # Poll every 200ms 


