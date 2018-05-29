# hello.py
from flask import Flask,redirect
app=Flask(__name__)
@app.route("/")
def index():
	return "<h1>hello world</h1>",302,{"Location":"http://www.google.com"}
@app.route("/redirect")
def red():
	return redirect("http://www.google.com")

if __name__=="__main__":
	app.run(threaded=True,debug=True)
