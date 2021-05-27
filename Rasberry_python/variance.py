# Variance
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED=22
BUTTON=4
BUTTON_PRESSED=0
ON=1
OFF=0

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN)
while 1:
    if(GPIO.input(BUTTON)==BUTTON_PRESSED):
        GPIO.ouput(LED,ON)
    else:
        GPIO.output(LED,OFF)
    button_value=GPIO.input(BUTTON)

    if(button_value==BUTTON_PRESSED) :
        GPIO.output(LED,ON)
    else:
        GPIO.output(LED,OFF)
# LED is operated when button is not pressed
button_value=GPIO.input(BUTTON)

if(button_value==BUTTON_PRESS):
    GPIO.output(LED.ON)
else:
    GPIO.output(LED,OFF)
