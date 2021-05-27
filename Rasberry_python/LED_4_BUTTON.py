# when Button is pressed, All LED is lighted
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_0=22
LED_1=23
LED_2=24
LED_3=25

BUTTON=4
BUTTON_PRESSED=0
ON=1
OFF=0

GPIO.setup(LED_0,GPIO.OUT)
GPIO.setup(LED_1,GPIO.OUT)
GPIO.setup(LED_2,GPIO.OUT)
GPIO.setup(LED_3,GPIO.OUT)

GPIO.setup(BUTTON,GPIO.IN)

while 1:
    if(GPIO.input(BUTTON)==BUTTON_PRESSED):
        GPIO.output(LED_0,1)
        GPIO.output(LED_1,1)
        GPIO.output(LED_2,1)
        GPIO.output(LED_3,1)
    else:
        GPIO.output(LED_0,0)
        GPIO.output(LED_1,0)
        GPIO.output(LED_2,0)
        GPIO.output(LED_3,0)