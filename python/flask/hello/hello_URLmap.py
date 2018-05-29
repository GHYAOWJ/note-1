# hello.py
from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
	return "<h1>hello world</h1>"
@app.route("/users")
def get_gusers():
	users=["Andy","Bill"]
	resp=["<p>{}</p>".format(user) for user in users]
	resp="\n".join(resp)
	return resp

if __name__=="__main__":
	app.run()
