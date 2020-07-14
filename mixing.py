#!/usr/bin/env python

import os
import time
import datetime
import glob
import mysql.connector
from time import strftime
import RPi.GPIO as GPIO
import random

#Variables for MySQL
db = mysql.connector.connect(host="10.10.1.254",port="3333", user="admin_iotfutami", passwd="futami17", db="admin_iotfutami") # replace password with your password
cur = db.cursor()

def id_sensor():
        var1 = "MIXING"
        return var1

def sensorProduction():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        if not GPIO.input(26):
                numr = random.randint(200, 225)
                pascals = numr
        else:
                numr = random.randint(75, 100)
                pascals = numr
        GPIO.cleanup()
        return pascals

def sensorCIP():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        numr2 = random.randint(200, 225)
        if not GPIO.input(25):
                numr = random.randint(200, 225)
                pascals = numr
        else:
                numr = random.randint(75, 100)
                pascals = numr
        GPIO.cleanup()
        return pascals

def note():
        notenya = "ini test input dari raspbery"
        return notenya

channels1 = "1"
channels2 = "2"
channels3 = "3"
channels4 = "4"
channels5 = "5"
id_sensors = id_sensor()
sensorCIPs = sensorCIP()
sensorProductions = sensorProduction()
notes = note()

sql1 = ("""INSERT INTO fyp (id_sensor,channel,sensor_read,note) VALUES (%s,%s,%s,%s)""", (id_sensors, channels1, sensorProductions, notes))
sql2 = ("""INSERT INTO fyp (id_sensor,channel,sensor_read,note) VALUES (%s,%s,%s,%s)""", (id_sensors, channels2, sensorCIPs, notes))
sql3 = ("""INSERT INTO fyp (id_sensor,channel,sensor_read,note) VALUES (%s,%s,%s,%s)""", (id_sensors, channels3, sensorProductions, notes))
sql4 = ("""INSERT INTO fyp (id_sensor,channel,sensor_read,note) VALUES (%s,%s,%s,%s)""", (id_sensors, channels4, sensorProductions, notes))
sql5 = ("""INSERT INTO fyp (id_sensor,channel,sensor_read,note) VALUES (%s,%s,%s,%s)""", (id_sensors, channels5, sensorProductions, notes))
try:
    print "Writing to the database..."
    cur.execute(*sql1)
    cur.execute(*sql2)
    cur.execute(*sql3)
    cur.execute(*sql4)
    cur.execute(*sql5)
    db.commit()
    print "Write complete"

except:
    db.rollback()
    print "We have a problem"

cur.close()
db.close()

#print secs
#print temperature
#print pressure
#print humidity
