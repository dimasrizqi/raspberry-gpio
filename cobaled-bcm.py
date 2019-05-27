import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

GPIO.output(19, GPIO.HIGH)
sleep(5)
GPIO.output(19, GPIO.LOW)
GPIO.cleanup()
