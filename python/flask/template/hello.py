# hello.py
from flask import Flask,render_template

app=Flask(__name__,template_folder="temp")

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/user/<name>")
def user(name):
	return render_template("user.html",name=name)
@app.route("/test")
def test():
	mydict={"key": "this is a secret"}
	mylist=[1,2,3,4]
	myintvar=0
	
	class Myobj():
		def method1(self):
			return "I'm a instance method"
		@staticmethod
		def method2():
			return "I'm a static method"
		@classmethod
		def method3(cls,value):
			return "I'm a class method, get value {}".format(value)

	context={
	"mydict":mydict,
	"mylist":mylist,
	"myintvar":myintvar,
	"instance":Myobj(),
	"class":Myobj
	}
	return render_template("test.html",**context)

registered_users=["maomao","alicia"]
@app.route("/ifelse/<name>")
def ifelse(name):
	if name not in registered_users:
		name=None
	return render_template("ifelse.html",name=name)
@app.route("/forloop")
def forloop():
	return render_template("forloop.html",users=registered_users)
@app.route("/macro")
def macro():
	return render_template("macro.html",users=registered_users)
@app.route("/import")
def himport():
	return render_template("import.html",users=registered_users)
@app.route("/extends")
def hextends():
	return render_template("extends.html") 

if __name__=="__main__":
	app.run(debug=True)
