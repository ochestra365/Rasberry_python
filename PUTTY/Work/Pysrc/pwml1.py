import RPi.GPIO as GPIO
import time

pwmPin =21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)

p=GPIO.PWM(pwmPin,0.5)
p.start(1)
input("Press return to stop")
p.stop()

GPIO.cleanup()

