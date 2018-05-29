# hello.py
from flask import Flask,abort
app=Flask(__name__)

def load_user(uid):
	try:
		uid=int(uid)
		if uid==1:
			return "Andy"
		elif uid==2:
			return "Bill"
	except BaseException:
		return

@app.route("/")
def index():
	return "<h1>hello world</h1>"
@app.route("/user/<uid>")
def get_user(uid):
	user=load_user(uid)
	if not user:
		abort(400)
	else:
		return "<h1>Hello, {}</h1>".format(user)

if __name__=="__main__":
	app.run()
