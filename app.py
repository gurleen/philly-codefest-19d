from flask import Flask, render_template, request, url_for, redirect
from dbloader import *
from resource_model import *
from volunteer_op_model import *

app = Flask(__name__)


@app.route('/')
def home():
    style = url_for('static', filename='css/flatly.css')
    return render_template('index.html', style=style)

@app.route('/resources/')
def resources():
    style = url_for('static', filename='css/flatly.css')
    results = get_resources_matching({})
    return render_template('list_view.html', results=results, style=style, title='Resources')

@app.route('/volunteer/')
def volunteers():
    style = url_for('static', filename='css/flatly.css')
    results = get_Volunteer_Ops_matching({})
    return render_template('list_view.html', results=results, style=style, title='Volunteer')

@app.route('/submit/', methods=['POST'])
def submit():
    result = request.form
    if result['sub_type'] == 'vol_op':
        x = Volunteer_Op(result['name'], result['loc'], result['descrip'], result['email'])
        store_Volunteer_Op(x)
        return redirect(url_for('volunteers'))
    else:
        x = Resource(result['name'], result['category'], result['loc'], result['descrip'], result['email'])
        store_resource(x)
        return redirect(url_for('/resources'))

@app.route('/about')
def about():
    style = url_for('static', filename='css/flatly.css')
    return render_template('about.html', style=style)