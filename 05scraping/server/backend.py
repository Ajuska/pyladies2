#!/usr/bin/python

### generate fake data

from faker import Faker
def generate_data():
	f = Faker('cs_CZ')

	for i in range(50):
		yield {
			'name': f.name(),
			'username': f.user_name(),
			'email': f.email(),
			'phone': f.phone_number(),
			'address': f.address(),
		}

data = list(generate_data())
data.sort(key=lambda x: x['name'])

### run webapp

from flask import Flask, render_template, abort
app = Flask(__name__)

@app.route('/')
def list():
	return render_template('list.html', data=data)

@app.route('/user/<username>/')
def profile(username):
	for person in data:
		if person['username'] == username:
			return render_template('profile.html', person=person)
	else:
		abort(404)

@app.route('/sitemap.xml')
def sitemap():
	return render_template('sitemap.xml', data=data)
