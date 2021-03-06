
from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def signup_refugee(name, email, password, gender, age):
	refugee_object = Refugee(
		name=name,
		email=email,
		password=password,
		gender=gender,
		age=age)
	session.add(refugee_object)
	session.commit()

def signup_volunteer(name, email, password, gender, age):
	volunteer_object = Volunteer(
		name=name,
		email=email,
		password=password,
		gender=gender,
		age=age)
	session.add(volunteer_object)
	session.commit()

def add_story(name, email, age, content):
	story_object = Story(
		name=name,
		email=email,
		age=age,
		content=content)
	session.add(story_object)
	session.commit()

def add_activity(name, description, age, date, location, leader)
	activity_object = Activity(
		name=name,
		description=description,
		age=age,
		date=date,
		location=location,
		leader=leader)
	session.add(activity_object)
	session.commit()

def query_refugee_by_email(email):
	refugee = session.query(Refugee).filter_by(email=email).first()
	return refugee

def query_volunteer_by_email(email):
	volunteer = session.query(Volunteer).filter_by(email=email).first()
	return volunteer

def query_all_stories():
	stories = session.query(Story).all()
	return stories

def query_all_activities():
	activities = session.query(Activity).all()
	return activities
