import RPi.GPIO as GPIO
import datetime
from time import sleep

#now = datetime.datetime.now()
#print ("jam skrng %s") % (now.hour)

lxon = "17:25"
lxoff = "05:30"

relay_pin_biru = 13
relay_pin_ijo = 6
relay_pin_ungu = 19
relay_pin_abu = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin_biru, GPIO.OUT)
GPIO.output(relay_pin_biru, 1)
GPIO.setup(relay_pin_ijo, GPIO.OUT)
GPIO.output(relay_pin_ijo, 1)
GPIO.setup(relay_pin_ungu, GPIO.OUT)
GPIO.output(relay_pin_ungu, 1)
GPIO.setup(relay_pin_abu, GPIO.OUT)
GPIO.output(relay_pin_abu, 1)
i = 1
try:
    while i == 1:
        time_skr = datetime.datetime.now().strftime("%H:%M")
        if time_skr <= lxoff or time_skr >= lxon:
                GPIO.output(relay_pin_ijo, 0)
                sleep(2)
                GPIO.output(relay_pin_biru, 0)
                sleep(2)
                GPIO.output(relay_pin_ungu, 0)
                sleep(2)
                GPIO.output(relay_pin_abu, 0)
#               print (time_skr)
#               print ("diantara lx on dan lx of")
        else:
#               print (time_skr)
#               print ("diliarnya")
                GPIO.output(relay_pin_ijo, 1)
                sleep(2)
                GPIO.output(relay_pin_biru, 1)
                sleep(2)
                GPIO.output(relay_pin_ungu, 1)
                sleep(2)
                GPIO.output(relay_pin_abu, 1)
        #basic
#       if time_skr == lxon:
#               GPIO.output(relay_pin_biru, 0)
#       if time_skr == lxoff:
#               GPIO.output(relay_pin_biru, 1)
except KeyboardInterrupt:
        pass
        i=0
GPIO.cleanup()
