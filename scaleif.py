import RPi.GPIO as GPIO
import time

p=21
Melody=[262,294,330,349,392,440,494,523]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p,GPIO.OUT)
B=GPIO.PWM(p,440)
try:
	while True:
		B.start(50)
		if res=='1':
			B.ChangeFrequency(Melody[0])
			time.sleep(0.1)
			B.stop()
			time.sleep(1)
		elif res=='2':
			B.ChangeFrequency(Melody[1])
			time.sleep(0.1)
			B.stop()
			time.sleep(1)
		elif res=='3':
			B.ChangeFrequency(Melody[1])
			time.sleep(0.1)
			B.stop()
			time.sleep(1)
			break
except KeyboardInterrupt:
	GPIO.cleanup()
