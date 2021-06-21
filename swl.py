#-*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch = 6	#입력핀설정

GPIO.setmode(GPIO.BCM) #BCM모드 사용

GPIO.setup(switch, GPIO.IN) #핀모드(입력)

try:
	while True:
		if GPIO.input(switch)== True:
			print("Pushed")
			time.sleep(0.3) #소프트웨어적으로 디바운싱함

except KeyboardInterrupt:
	GPIO.cleanup()
