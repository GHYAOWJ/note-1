# hello.py
from time import sleep
from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
	sleep(10)
	return "<h1>hello world</h1>"
@app.route("/test")
def test():
	return "<h1>test</h1>"

if __name__=="__main__":
	app.run(threaded=True,debug=True)
