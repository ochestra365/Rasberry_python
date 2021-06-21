#-*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pinNum = 15

#도 레 미 파 솔 라 시 도 레 미 파
melody = [ 262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 699 ]

GPIO.setup(pinNum, GPIO.OUT)
p = GPIO.PWM(pinNum, 100) #채널과주파수

try:
	while True : #무한루프이다
		num = int(input("keyboard num 1-11 : "))-1 #배열을 써줄것이다
		p.ChangeFrequency(melody[num]) #
		p.start(100)
		p.ChangeDutyCycle(90) 
		time.sleep(0.5)
		p.stop() 
except KeyboardInterrupt: 
	GPIO.cleanup()
