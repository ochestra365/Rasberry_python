#-*-coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch = 6
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(switch, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
signal=True
def swBlink(channel):
try:
	while True:
		global flag
		if GPIO.input(switch)==True:
			print("interrupt")
			GPIO.output(switch, signal)
			flag = True 
		else:
			flag=False
			
GPIO.add_event_detect(switch, GPIO.RISING, callback=swBlink)
try: 
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()


