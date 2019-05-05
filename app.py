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
    return render_template('list_view.html', results=results, style=style, title='Resources', is_res=True)

@app.route('/volunteer/')
def volunteers():
    style = url_for('static', filename='css/flatly.css')
    results = get_Volunteer_Ops_matching({})
    return render_template('list_view.html', results=results, style=style, title='Volunteer', is_res=False)

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

# /view?id=abc
@app.route('/view-res/')
def view_res():
    style = url_for('static', filename='css/flatly.css')
    res_id = request.args.get('id')
    result = get_resources_matching({'_id': res_id})
    if result == None:
        return redirect(url_for('home'))
    else:
        return render_template('individual.html', style=style, info=result[0].get_json(), is_res=True)

@app.route('/view-vol/')
def view_vol():
    style = url_for('static', filename='css/flatly.css')
    vol_id = request.args.get('id')
    result = get_Volunteer_Ops_matching({'_id': vol_id})
    if result == None:
        return redirect(url_for('home'))
    else:
        return render_template('individual.html', style=style, info=result[0].get_json(), is_res=False)


@app.route('/about')
def about():
    style = url_for('static', filename='css/flatly.css')
    return render_template('about.html', style=style)