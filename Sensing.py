import RPi.GPIO as GPIO
import time

s2=23
s3=24
out=25

# NUM_CYCLES=10

def read_value(a0,a1):
	GPIO.output(s2,a0)
	GPIO.output(s3,a1)
	time.sleep(0.1)

	GPIO.wait_for_edge(out,GPIO.FALLING)
	GPIO.wait_for_edge(out,GPIO.RISING)
	start=time.time()
	GPIO.wait_for_edge(out,GPIO.FALLING)
	return (time.time()-start)*1000000

#def send_data(result):

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(out,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	GPIO.setup(s2,GPIO.OUT)
	GPIO.setup(s3,GPIO.OUT)

def loop():
	result=""

	while True:
		r=read_value(GPIO.LOW,GPIO.LOW)
		time.sleep(0.1)
		g=read_value(GPIO.HIGH,GPIO.HIGH)
		time.sleep(0.1)
		b=read_value(GPIO.LOW,GPIO.HIGH)

		print('red={0}, green={1}, blue={2}'.format(r,g,b))

		if r>200000 and g>200000 and b>180000:
			result="BLACK"
		else:
			if(b<g)and(b<r):
				result="BLUE"
			elif (g<b) and (g<r):
				result="GREEN"
			elif(r<g) and (r<b):
				result="RED"
		print(result)
		time.sleep(1)

if __name__=='__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()
