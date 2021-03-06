import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pinNum=14

melody=[262,294,330,349,392,440,494,523,587,659,699]

GPIO.setup(pinNum,GPIO.OUT)
p=GPIO.PWM(pinNum,100)

try:
    while True:
        num=int(input("keyboard num 1-11 : "))-1
        p.ChangeFrequency(melody[num])
        p.start(100)
        p.ChangeDutyCycle(90)
        time.sleep
        p.stop()
except KeyboardInterrupt:
    GPIO.cleanup()
