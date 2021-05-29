from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)


ledPin=14
speakerPin=15
pinPiezo=2
triggerPin=26
echoPin=19

melody=[262,294,330,349,392,440,494,523,587,659,699]
melody_rabbit=[294, 440,392,349, 330, 294, 262, 294, 440, 494, 523, 523, 494, 440, 392, 440, 294, 440, 392, 349, 330, 294, 262 , 294, 294, 330, 349, 330, 294, 262 , 330, 294, 349, 392, 440, 523, 494, 440, 392, 440, 349, 440, 392, 349, 392, 440, 262 , 294, 262 , 494, 440, 349, 392, 440, 523, 494, 440, 392, 440, 349, 440, 392, 294, 330, 349, 330, 349, 392, 349, 392, 440, 294, 440, 392, 349, 330, 294, 262 , 294, 440, 494, 523, 523, 494, 440, 392, 440, 294, 440, 392, 349, 330, 294, 262 , 294, 294, 330, 349, 330, 294, 262 , 330, 294]
melody_ts=[440, 262 , 294, 294, 349, 392, 440, 523, 440, 392, 349, 294, 440, 392, 294, 440, 392, 294, 262 , 440, 440, 262 , 294, 294, 349, 392, 440, 262 , 440, 392, 349, 294, 440, 392, 294, 440, 392, 294, 262 , 294, 440, 262 , 294, 294, 262 , 294, 330, 262 , 294, 262 , 392, 440, 440, 262 , 294, 294, 262 , 294, 349, 330, 262 , 440, 440, 262 , 294, 262 , 294, 330, 262 , 294, 262 , 392, 440, 440, 392, 294, 440, 392, 294, 262 , 294, 440, 262 , 294, 294, 262 , 294, 330, 262 , 294, 262 , 392, 440, 440, 262 , 294, 294, 262 , 294, 349, 330, 262 , 440, 440, 262 , 294, 294, 262 , 294, 330, 262 , 294, 262 , 392, 440, 440, 392, 294, 440, 392, 294, 262 , 294,]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(speakerPin,GPIO.OUT)
GPIO.setup(triggerPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)
GPIO.setup(pinPiezo,GPIO.OUT)

p=GPIO.PWM(speakerPin,100)
Buzz=GPIO.PWM(pinPiezo,440)

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
			while True:
				num=int(input("keyboard num 1-11 : "))-1
				print(num)
				p.ChangeFrequency(melody[num])
				p.start(100)
				p.ChangeDutyCycle(90)
				time.sleep(0.5)
				p.stop()
	elif data=="Legacy of rabbit living on the moon":
            while True:
                p.start(50)
                for i in range(0,len(melody_rabbit)):
                    p.ChangeFrequency(melody_rabbit[i])
                    time.sleep(0.3)
                p.stop()
                time.sleep(1)
	elif data=="Ultra":
		while True:
			GPIO.output(triggerPin, GPIO.LOW)
			time.sleep(0.00001)
			GPIO.output(triggerPin,GPIO.HIGH)
			
			while GPIO.input(echoPin)==GPIO.LOW:
				start = time.time()
			while GPIO.input(echoPin)==GPIO.HIGH:
				stop=time.time()
			rtTotime=stop-start
			distance=rtTotime*34000/2
			print("distance : %2f cm"%distance)
			time.sleep(1)
			 
if __name__=="__main__":
	app.run(host="0.0.0.0",port="8080")

