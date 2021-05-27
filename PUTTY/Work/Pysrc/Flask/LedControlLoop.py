#!/usr/bin/env python3.7
import RPi.GPIO as GPIO
import time

LED21=21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED21,GPIO.OUT)

try:
	while True:
		GPIO.output(LED21,True)
		time.sleep(1)
		GPIO.output(LED21,False)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()

