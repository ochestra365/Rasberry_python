import RPi.GPIO as GPIO
import time

LED21=21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED21,GPIO.OUT)

try:
	for i in range(20):
		if i%2==0:
			GPIO.output(LED21,True)
			time.sleep(1)
		if i%2 !=0:
			GPIO.output(LED21,False)
			time.sleep(1)
				
except KeyboardInterrupt:
	GPIO.cleanup()
