#!/bin/bash
modprobe uinput
nohup python /home/pi/gpio/gpioenter.py &
