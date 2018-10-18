import numpy as np
import random
import operator
import json

skills = ['Translation (Chinese and English)', 'Fundraising', 'Graphic Design', 'Web Design',
 'Editorial', 'Admin', 'Events', 'PR/Marketing/Social Media', 'Sharing your story/lived experience',
 'IT/Technology']

#The probability of the users mastered with the certain skills listed above
skills_probability = [0.90, 0.50, 0.30, 0.20, 0.60, 0.70, 0.80, 0.50, 0.70, 0.30]
preferred_skills = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
event_hours = 8
class user():
	def __init__(self):
		self.skills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for i in range(10):
			rand_number = random.randint(1, 101)
			if (rand_number < skills_probability[i] * 100):
				self.skills[i] = 1
		self.available_hours = random.randint(1, 11)
		self.past_experience = random.randint(0, 4)
	def set_user_id(self, id_number):
		self.user_id = id_number


def calculate_user_availability_score(user_hours,event_hours):
	percentage_of_hours=user_hours/event_hours
	return percentage_of_hours

def calculate_user_experience_score(user_experiences):
	return float((0.5+user_experiences)/3)

def calculate_user_skills_score(user_skills, preferred_skills):
	match_count = 0
	needed_count = 0
	for i in range(len(user_skills)):
		if preferred_skills[i] == 1:
			needed_count += 1
			if user_skills[i] == 1:
				match_count += 1
	percentage_of_skill_satisfied = match_count/needed_count
	return percentage_of_skill_satisfied


def calculate_overall_scores(user_skills_score, user_experience_score, user_availability_score):
    return(round(user_skills_score*user_experience_score*user_availability_score, 3))


def calculate_score_recommendation(preferred_skills, event_hours):
	volunteer_info = {}
	with open ('volunteer_info.json', 'r') as f:
		volunteer_info = f.read()
	f.close()
	volunteer_list = json.loads(volunteer_info)
	for volunteer in volunteer_list:
		volunteer['score'] = calculate_overall_scores(
			calculate_user_skills_score(volunteer['skills'], preferred_skills),
			calculate_user_experience_score(volunteer['past_experience']), 
			calculate_user_availability_score(volunteer['available_hours'], event_hours))
	sorted_volunteer_list = sorted(volunteer_list, key = operator.itemgetter('score'))
	recommendation_id_list = []
	for i in range(5):
		recommendation_id_list.append(sorted_volunteer_list[-(i+1)]['id'])
	return (recommendation_id_list)


calculate_score_recommendation(preferred_skills, event_hours)