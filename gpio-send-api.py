#!/usr/bin/env python

import os
import time
import datetime
import glob
from time import strftime
import RPi.GPIO as GPIO
import random
import requests


def sensorSterilization():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if not GPIO.input(18):
                numr = random.randint(200, 225)
                val = numr
        else:
                numr = random.randint(75, 100)
                val = numr
        GPIO.cleanup()
        return val

def sensorProduction():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if not GPIO.input(26):
                numr = random.randint(200, 225)
                val = numr
        else:
                numr = random.randint(75, 100)
                val = numr
        GPIO.cleanup()
        return val

def sensorCIP():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        numr2 = random.randint(200, 225)
        if not GPIO.input(25):
                numr = random.randint(200, 225)
                val = numr
        else:
                numr = random.randint(75, 100)
                val = numr
        GPIO.cleanup()
        return val

def sensorTank1():
        # numr = random.randint(8000, 12000)
        # val = numr
        # return val

def sensorTank2():
        # numr = random.randint(8000, 12000)
        # val = numr
        # return val

id_sensors = "MIXING"
sensorCIPs = sensorCIP()
sensorProductions = sensorProduction()
sensorSterilizations = sensorSterilization()
sensorTank1s = sensorTank1()
sensorTank2s = sensorTank2()

try:
#    print "Writing to the database..."
    requests.post("http://103.30.244.22:8000/api/iots",data={'sensor':id_sensors,'channel':'1','value':sensorCIPs})
    requests.post("http://103.30.244.22:8000/api/iots",data={'sensor':id_sensors,'channel':'2','value':sensorProductions})
    requests.post("http://103.30.244.22:8000/api/iots",data={'sensor':id_sensors,'channel':'3','value':sensorSterilizations})
    requests.post("http://103.30.244.22:8000/api/iots",data={'sensor':id_sensors,'channel':'4','value':sensorTank1s})
    requests.post("http://103.30.244.22:8000/api/iots",data={'sensor':id_sensors,'channel':'5','value':sensorTank2s})
   

except:
    
    print "We have a problem"

