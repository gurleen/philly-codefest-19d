from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/resources/')
def resources():
    return 'Resources page'

@app.route('/volunteer/')
def volunteers():
    return 'Volunteer page'

@app.route('/submit-resource/', methods=['POST', 'GET'])
def submit_resource():
    return 'Submit resource'

@app.route('/submit-volunteer/', methods=['POST', 'GET'])
def submit_volunteer():
    return 'Submit volunteer'

@app.route('/about')
def about():
    return 'About us'