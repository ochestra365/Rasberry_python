import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED=22

GPIO.setup(LED,GPIO.OUT)

while 1:
        GPIO.output(LED,1)
        time.sleep(3)
        GPIO.output(LED,0)
        time.sleep(2)
