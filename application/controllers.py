from flask import Flask, render_template, request
from application import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods = ['POST'])
def generate_proposal():
    data = {
        'client_name': request.form['client_name'],
        'client_industry': request.form['client_industry'],
        'project_goal': request.form['project_goal'],
        'target_audience': request.form['target_audience'],
        'timeline': f"{request.form['start_date']} - {request.form['end_date']}",
        'budget_range': request.form['budget_range'],
        'tech_pref': request.form['tech_pref'],
        'tone': request.form['tone'],
    }

    print(data)