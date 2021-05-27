import RPi.GPIO as GPIO
import time

led = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

try:
	while True:
		GPIO.output(led,True) # 풀다운 저항이 기본이라 1값이 먹힌다
		time.sleep(1)
		GPIO.output(led,False)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
