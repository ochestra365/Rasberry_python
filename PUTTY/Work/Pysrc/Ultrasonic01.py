#-*- coding: utf-8-*-
import RPi.GPIO as GPIO
import time

pinPiezo=21
triggerPin = 14
echoPin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin,GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(pinPiezo,GPIO.OUT)

Buzz=GPIO.PWM(pinPiezo,440)


try:
	while True:
		GPIO.output(triggerPin, GPIO.LOW) #출력핀이기 때문이다
		time.sleep(0.00001)
		GPIO.output(triggerPin, GPIO.HIGH)

		while GPIO.input(echoPin) == GPIO.LOW: #입력핀이기 떄문이다.
			start = time.time()
		while GPIO.input(echoPin) == GPIO.HIGH:
			stop = time.time()
		rtTotime = stop - start
		distance = rtTotime * 34000 / 2
		print("distance : %.2f cm "%distance)
		time.sleep(1)

		if distance <= 30 and distance > 20:
			while True:
				Buzz.start(50)
				Buzz.ChangeFrequency(262)
				time.sleep(2)
				Buzz.stop()
				time.sleep(2)
				
				GPIO.output(triggerPin,GPIO.LOW)
				time.sleep(0.00001)
				GPIO.output(triggerPin,GPIO.HIGH)

				while GPIO.input(echoPin)==GPIO.LOW:
					start=time.time()
				while GPIO.input(echoPin)==GPIO.HIGH:
					stop=time.time()
					
				rtTotime=stop - start
				distance = rtTotime * 34000/2
				print("distance : %.2f cm"%distance)
				time.sleep(1)
				if distance < 20:
					break

		elif distance <= 20 and distance>10:
			while True:
				Buzz.start(50)
				Buzz.ChangeFrequency(294)
				time.sleep(1)
				Buzz.stop()
				time.sleep(1)

				GPIO.output(triggerPin,GPIO.LOW)
				time.sleep(0.00001)
				GPIO.output(triggerPin,GPIO.HIGH)

				while GPIO.input(echoPin)==GPIO.LOW:
					start=time.time()
				while GPIO.input(echoPin)==GPIO.HIGH:
					stop=time.time()

				rtTOtime=stop-start
				distance = rtTotime*34000/2
				print("distance: %.2f cm"%distance)
				time.sleep(1)
				if distance < 10:
					break
					
		elif distance <= 10:
			while True:
				Buzz.start(50)
				Buzz.ChangeFrequency(392)
				time.sleep(0.5)
				Buzz.stop()
				time.sleep(0.5)

				GPIO.output(triggerPin,GPIO.LOW)
				time.sleep(0.0001)
				GPIO.output(trigger,GPIO.HIGH)

				while GPIO.input(echoPin)==GPIO.LOW:
					start=time.time()
				while GPIO.input(echoPin)==GPIO.HIGH:
					stop=time.time()

				rtTotime=stop-start
				distance = rtTotime * 34000/2
				print("distance : %.2f cm"%distance)
				time.sleep(1)
				if distance < 3:
					break

except KeyboardInterrupt:
	GPIO.cleanup()


