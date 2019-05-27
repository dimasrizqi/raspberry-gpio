import RPi.GPIO as GPIO

ch1 = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while 1:
		if GPIO.input(ch1):
			print("DIPENCET")
		else:
			print("DILEPAS")
except KeyboardInterrupt:
	GPIO.cleanup()
