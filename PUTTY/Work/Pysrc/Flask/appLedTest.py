
from flask import Flask
import RPi.GPIO as GPIO

app=Flask(__name__) #객체생성

ledPin = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


@app.route('/')
def flask():
	return "Hello Flask"
@app.route('/led/on')
def ledOn():
	GPIO.output(ledPin,True) #한번켜지는 명령을 계속주는 것이다
	return "<h2>Led ON</h2>"

@app.route('/led/off')
def ledOff():
	GPIO.output(ledPin,False) #한 번 꺼지는 명령을 계속 주는 것이다
	return "<h2>Led off</h2>"

@app.route('/led/clean')
def clean():
	GPIO.cleanup()
	return "<h1>GPIO Clean</h1>"

if __name__=="__main__":
	app.run(host="0.0.0.0",port="8080")

