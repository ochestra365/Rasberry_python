#LED is operated when both button is pressed
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED=22
BUTTON_0=4
BUTTON_1=5
BUTTON_PRESSED=0
ON=1
OFF=0

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON_0,GPIO.IN)
GPIO.setup(BUTTON_1,GPIO.IN)

while 1:
    GPIO.setup(BUTTON_0,GPIO.IN)
    GPIO.setup(BUTTON_1,GPIO.IN)

    while 1:
        but0_value =GPIO.input(BUTTON_0)
        but1_value=GPIO.input(BUTTON_1)

        if((but0_value==BUTTON_PRESSED)and(but1_value==BUTTON_PRESSED)):
            GPIO.output(LED,ON)
        else:
            GPIO.output(LED,OFF)
