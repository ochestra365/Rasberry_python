#-*-coding: utf-8-*-

import RPi.GPIO as GPIO #라즈베리파이 이용

ledPin=14 #21번 포트 사용
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO넘버읽겠다
GPIO.setup(ledPin,GPIO.OUT) #출력을 담당한다

p=GPIO.PWM(ledPin,255) #파장은 255까지(Pulse Width Modulation) 

p.start(0) #0값부터 시작전달되는 객체를 통해 시행한다

while True:
	d=input("Enter Brightness(0 to 100) : ")
	duty = int(d)

	if(duty==100):
		p.stop()
		GPIO.cleanup()
		break
	else:
		p.ChangeDutyCycle(duty)
