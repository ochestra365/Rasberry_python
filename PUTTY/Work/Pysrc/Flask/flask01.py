from flask import Flask
import RPi.GPIO as GPIO

app=Flask(__name__)

ledPin=21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

@app.route('/')
def flask():
	return "Hello Flask"
@app.route('/led/<state>')
def led(state):
	if state == "on":
		GPIO.output(ledPin,True)
	else:
		GPIO.output(ledPin,False)
	return "LED"+state
@app.route('/led/clean')
def clean():
	GPIO.cleanup()
	return "<h1> GPIO CLEANUP </h1>"

if __name__=="__main__":
	app.run(host="0.0.0.0",port="8080")


