import RPi.GPIO as GPIO
import time
import keyboard

pin=21
Melody = [262,294,330,349,392,440,494,523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

Buzz=GPIO.PWM(pin,440)

try:
	while True:
			Buzz.start(50)
			for i in range(0,len(Melody)):
				Buzz.ChangeFrequency(Melody[i])
				time.sleep(0.3)
			Buzz.stop()
			time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
