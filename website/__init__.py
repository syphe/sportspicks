from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World"

@app.route("/login/", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
 	else:
 		return "POST";

@app.route("/ladder/")
def ladder():
  return "This is a ladder"