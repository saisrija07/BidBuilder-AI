from flask import Flask, render_template, request
from application import app
import json

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_proposal', methods = ['POST'])
def generate_proposal():
    if request.method == 'POST':
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
        
        with open('sample_output.json') as f:
            context = f.read()
            context = json.loads(context)

        return render_template('proposal.html', data = context)