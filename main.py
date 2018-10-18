from threading import Thread
from datetime import datetime
from time import sleep
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
# from .database import dbhelper
app = Flask(__name__)
db_instance = None

@app.route("/")
def index_page():
	return render_template('index.html')
@app.route('/register', methods=['POST'])
def register_post():
	username = request.form.get('username')
	# db_instance.insert_many(doc_name,docs)

if __name__ == '__main__':
	# separate thread to call multiple functions at regular period
	'''
	thread=routineThread(1)
	thread.start()
	'''

	print("Server has started")
	app.config.from_pyfile('config.py')
	app.config["JSON_AS_ASCII"] = False
	# app.run(debug=False)
	app.run(host= '0.0.0.0')
	#db_instance = dbhelper()
	#db_instance.setup()
