# main.py

from flask import Flask

app = Flask(_name_)

@app.route("/")
def index():
	return "Congratulations, it's a web app!"
