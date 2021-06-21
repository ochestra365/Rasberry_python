from flask import Flask

app = Flask(__name__)

@app.route('/name')
def name():
	return "<h1> My name is PSC</h1>"
@app.route('/name/age')
def age():
	return "<h1>i'm 28 years old</h1>"

if __name__=="__main__":
	app.run(host="0.0.0.0", port="8080")
