import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
sleep(5)
GPIO.output(12,GPIO.LOW)
GPIO.cleanup()
