import RPi.GPIO as GPIO
from time import sleep

relay_pin_biru = 13
relay_pin_ijo = 6
relay_pin_ungu = 19
relay_pin_abu = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin_biru, GPIO.OUT)
GPIO.output(relay_pin_biru, 1)
GPIO.setup(relay_pin_ijo, GPIO.OUT)
GPIO.output(relay_pin_ijo, 1)

try:
    while True:
        GPIO.output(relay_pin_biru, 1)
#        sleep(1)
        GPIO.output(relay_pin_ijo, 0)
        sleep(1)
        GPIO.output(relay_pin_biru, 0)
#        sleep(1)
        GPIO.output(relay_pin_ijo, 1)
        sleep(1)

except KeyboardInterrupt:
        pass
GPIO.cleanup()
