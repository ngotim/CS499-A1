from flask import render_template
from app import app

@app.route('/')
def index():
	retD = {}
	retD['user'] = 'Timothy'
	retD['title'] = 'Home'
	return render_template("index.html", **retD)

