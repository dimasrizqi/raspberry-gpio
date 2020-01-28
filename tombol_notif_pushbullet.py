import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)  #GPIO.BCM uses the GPIO port name for reference

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.OUT)


# Boolean to keep track of the button
Enter = False

while True:
    if (not Enter) and (not GPIO.input(26)):      # Big Red Button pressed
        Enter = True
#       print("tekan biru")
        os.system("/home/pi/pushbullet-biru.sh")
    if Enter and GPIO.input(26):                      # Big Red Button released
        Enter = False
    if (not Enter) and (not GPIO.input(25)):      # Big Red Button pressed
        Enter = True
#        print("tekan orange")
        os.system("/home/pi/pushbullet-orange.sh")
    if Enter and GPIO.input(25):                      # Big Red Button released
        Enter = False

    time.sleep(0.1)                                           # Poll every 200ms

GPIO.cleanup()

