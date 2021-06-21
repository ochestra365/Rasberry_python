#-*coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch = 6
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #내부풀다운사용

def swBlink(channel): #callback 함수
	global flag
	if flag == False:
		print("interrupt")
		flag = True
	else:
		flag = False
#인터럽터편에 라이징 신호가 안가지면 콜백함수로 리턴되어 실행된다.
GPIO.add_event_detect(switch, GPIO.RISING, callback=swBlink)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
