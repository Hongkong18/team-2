from threading import Thread
from datetime import datetime
from time import sleep
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)
db_instance = None

@app.route("/")
def index_page():
	return render_template('index.html')
@app.route('/register', methods=['POST'])
def register_post():
	doc={'a':'b'}
	db_instance['main_db']['helpers'].insert_one(docs)
	return "Registered"
@app.route('/test')
def test_fun():
	db_instance['main_db']['helpers'].insert_many([{'name':'abc'}])
	return "3"

if __name__=="__main__":
	print("Server has started")
	db_instance = MongoClient('localhost',27017)
	app.run(debug=True)
	# app.run(host= '0.0.0.0')
	
