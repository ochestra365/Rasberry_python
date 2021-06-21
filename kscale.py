import RPi.GPIO as GPIO
import time

speaker=20
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(speaker,GPIO.OUT)
p=GPIO.PWM(speaker,440)

melody=[261,294,329,349,392,440,493,523]

try:
	while True:
		p.star(50)
		for i in range(0,len(melody)):
			p.ChangeFrequency(melody[i]
			time.sleep(0.3)
		p.stop()
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

