from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setwarnings(False)

@app.route('/')
def home():
	return render_template("index.html")
	
@app.route('/data', methods = ['POST'])
def data():
	data = request.form['led']
	if data == 'on':
		GPIO.output(ledPin,True)
	#	return render_template('on') 
		return home()
	elif data=='off':
		GPIO.output(ledPin,False)
	#	return  reder_template('off')
		return home()
		 
	elif data=="restart":
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(ledPin,GPIO.OUT)
		return home()
	elif data=="clean":
		GPIO.cleanup()
		return "cleanup"
if __name__ == "__main__":
	app.run(host="0.0.0.0",port="8080")
