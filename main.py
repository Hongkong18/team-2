from threading import Thread
from datetime import datetime
from time import sleep
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from pymongo import MongoClient
import volunteers
from volunteers import calculate_score_recommendation
import json


app = Flask(__name__)
db_instance = None

@app.route("/")
def index_page():
	return render_template('index.html')

@app.route('/registration')
def register():
	return render_template('registration.html')


@app.route('/calendar')
def event_calendar():
	return render_template('/calendar/demos/agenda-views.html')

@app.route('/dashboard_event')
def dashboard_page():
	return render_template('Events.html')

@app.route('/event_assignment')
def calendar():
	return render_template('eventAssignment.html')

@app.route('/partners')
def partners():
	return render_template('Partners.html')

@app.route('/sponsor_form')
def sponsor_form():
	return render_template('sponsor_form.html')

@app.route('/sponsors')
def sponsor():
	return render_template('Sponsors.html')

@app.route('/staff')
def staff():
	return render_template('Staff.html')

@app.route('/volunteers')
def volunteer():
	return render_template('Volunteers.html')


@app.route('/dashboard_event/get_recommended_volunteer')
def get_recommended_volunteer():
	preferred_skills = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
	event_hours = 5
	recommendation_id_list = calculate_score_recommendation(preferred_skills, event_hours)
	post = {"recommendation": recommendation_id_list}
	to_be_written = json.dumps(post)
	file_path = 'static/recommendation.json'
	with open(file_path, 'w') as f:
		f.write(to_be_written)
	f.close()
	return json.dumps(post)



if __name__=="__main__":
	print("Server has started")
	client = MongoClient('localhost',27017)
	app.run(debug=True)
	# app.run(host= '0.0.0.0')
	
