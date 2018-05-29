# hello.py
from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def index():
	user_agent=request.headers.get("User-Agent")
	user_name=request.args.get("name")
	return "<p>Your browser is {}</p><p>Your name is {}</p>".format(user_agent,user_name)

if __name__=="__main__":
	app.run(threaded=True,debug=True)
