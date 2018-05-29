# hello.py
from flask import Flask,make_response
app=Flask(__name__)
@app.route("/")
def index():
	return "<h1>hello world</h1>"
@app.route("/no_cookie")
def no_cookie():
	response = make_response("<h1>This document doesn't carry a cookie !</h1>")
	return response
@app.route("/has_cookie")
def has_cookie():
	response=make_response("<h1>This document carries a cookie !</h1>")
	response.set_cookie("answer","42")
	return response

if __name__=="__main__":
	app.run()
