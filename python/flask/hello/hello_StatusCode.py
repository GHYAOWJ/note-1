# hello.py
from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
	return "<h1>hello world</h1>",400

if __name__=="__main__":
	app.run(threaded=True,debug=True)
