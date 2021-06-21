import RPi.GPIO as GPIO
import time
import keyboard

switch5 = 5
switch6 = 6
LED21 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch5,GPIO.IN)
GPIO.setup(switch6,GPIO.IN)
GPIO.setup(LED21, GPIO.OUT)
signal = True

try:
	while True:
		if GPIO.input(switch5) ==True:
			print("Pushed switch5)
			signal = not signal
			GPIO.output(LED21, siganl)
		if GPIO.input(switch6)==True:
			print("Pushed switch6)
			GPIO.output(LED21,signal)
			time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()
