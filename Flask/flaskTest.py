from flask import Flask

app = Flask(__name__) #__name__이름을이용한Flask 객체를 생성

@app.route('/') #클라이언트가 uri로 /를 요청하면
def hello(): #뷰함수가 실행이 된다.
	return "Hello Flask!!" #반드시return이 있어야 한다

if __name__=="__main__": #직접실행을위한조건
	app.run(host = "0.0.0.0",port="8080")
