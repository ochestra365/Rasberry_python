from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

ledPin=14
speakerPin=15
melody=[262,294,330,349,392,440,494,523,587,659,699]

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(speakerPin,GPIO.OUT)
p=GPIO.PWM(speakerPin,100)

GPIO.setwarnings(False)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/data', methods=['POST'])
def data():
	data = request.form['led']
	if data == 'on':
		GPIO.output(ledPin,True)
		return home()
	elif data=='off':
		GPIO.output(ledPin,False)
		return home()
	elif data=="restart":
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(ledPin,GPIO.OUT)
		return home()
	elif data=="clean":
		GPIO.cleanup()
		return "cleanup"
	elif data=="Piano":
#		try:
			while True:
				num=int(input("keyboard num 1-11 : "))-1
				print(num)
				p.ChangeFrequency(melody[num])
				p.start(100)
				p.ChangeDutyCycle(90)
				time.sleep(0.5)
				p.stop()
	#	except KeyboardInterrupt:
	#		GPIO.cleanup()
if __name__=="__main__":
	app.run(host="0.0.0.0",port="8080")


