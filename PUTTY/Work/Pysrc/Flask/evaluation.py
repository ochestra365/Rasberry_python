from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app=Flask(__name__)
###핀설정파트### 전략-->버스채널을 하드웨어적으로 사용할 것 VCC핀이 모자람
ledPin=26
pinPiezo= 2
triggerPin =3
echoPin=4

speakerPin=13
###셋업파트###
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
##LED셋업
GPIO.setup(ledPin,GPIO.OUT)
##초음파셋업
GPIO.setup(triggerPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)
GPIO.setup(pinPiezo,GPIO.OUT)
Buzz=GPIO.PWM(PinPiezo,440)
##피아노셋업
melody = [262,294,330,349,392,440,494,523,587,659,699]
GPIO.setup(speakerPin,OUT)
p=GPIO.PWM(speakerPin,100)
###LED###
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/data',methods=['POST'])
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
    elif data=="restart":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ledPin,GPIO.OUT)
        return home()
    elif data=="clean":
        GPIO.cleanup()
        return "cleanup"
 
###초음파###
@app.route('/data',methods=['POST'])
def Ultra():
    data = request.form['led']
    if Ultra =='Uon':
        try:
            while True:
                GPIO.output(triggerPin,GPIO.LOW)
                time.sleep(0.00001)
                GPIO.output(triggerPin, GPIO.HIGH)
                
                while GPIO.input(echoPin) == GPIO.LOW:
                    start = time.time()
                rtTotime=stop-start
                distance = rtTotime * 34000/2
                print("distance : %.2f cm"%distance)
                time.sleep(1)

                if distance <=30 and distance >20:
                    while True:
                        Buzz.start(50)
                        Buzz.ChangeFrequency(262)
                        time.sleep(2)
                        Buzz.stop()
                        time.sleep(2)
 
                        GPIO.output(triggerPin,GPIO.LOW)
                        time.sleep(0.00001)
                        GPIO.output(triggerPin,GPIO.HIGH)

                        while GPIO.input(echoPin)==GPIO.LOW:
                            start=time.time()
                        while GPIO.input(echoPin)==GPIO.HIGH:
                            stop.time.time()
 
                        rtTotime=stop-start
                        distance =rtTotime * 34000/2
                        print("distance : %.2f cm"%distance)
                        time.sleep(1)
                        if distance < 20:
                            break

                elif distance <= 20 and distance > 10:
                    while True:
                        Buzz.start(50)
                        Buzz.ChangeFrequency(294)
                        time.sleep(1)
                        Buzz.stop()
                        time.sleep(1)

                        GPIO.output(triggerPin,GPIO.LOW)
                        time.sleep(0.00001)
                        GPIO.output(triggerPin,GPIO.HIGH)

                        while GPIO.input(echoPin)==GPIO.LOW:
                            start=time.time()
                        while GPIO.input(echoPin)==GPIO.HIGH:
                            stop=time.time()

                        rtTotime=stop-start
                        distance = rtTotime*342000/2
                        print("distance: %.2f cm"%distance)
                        time.sleep(1)
                        if distance < 10:
                            break

                        elif distance <= 10:
                            while True:
                                Buzz.start(50)
                                Buzz.ChangeFrequency(392)
                                time.sleep(0.5)
                                Buzz.stop()
                                time.sleep(0.5)

                                GPIO.output(triggerPin,GPIO.LOW)
                                time.sleep(0.00001)
                                GPIO.output(triggerPin,GPIO.HIGH)

                                while GPIO.input(echoPin)==GPIO.LOW:
                                    start=time.time()
                                while GPIO.input(echoPin)==GPIO.HIGH:
                                    stop=time.time()

                                rtToTime = stop - start
                                distance = rtTotime * 34000/2
                                print("distance : %.2f cm"%distance)
                                time.sleep(1)
                                if distance < 3:
                                    break
# return home()
###GPIO클린해주기 및 키보드 간섭 배제 들여쓰기 문제 발생할 거 같으니까 고쳐볼것. 초음파 파트는 들여쓰기 return 문을 좀 더 잘 써줘야 할 것이다.
# except KeyboardInterrupt:
#  GPIO.cleanup()

##피아노 파트
@app.route('/data',methods=['POST'])
def piano():
    piano = request.form['led']
    if piano == 'Pon'
        while True:
            num = int(input("Keyboard num 1-11 : "))-1
            p.ChangeFrequency(melody[num])
            p.start(100)
            p.ChangeDutyCycle(90)
            time.sleep(0.5)
            p.stop()
        return home()
    elif piano== 'Prestart':
        return home()
    elif piano=="Pclean":
        GPIO.cleanup()
        return "cleanup"
 ###함수실행###
if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")

##연산 종료 시 GPIO의 내용을 휘발시켜서 다시 쓸 수 있게 함
except KeyboardInterrupt:
    GPIO.cleanup()


