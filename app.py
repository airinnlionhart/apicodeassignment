from flask import Flask, redirect, render_template, url_for, request
import models
import json
from logic import GetApplicants

Debug = True

app = Flask(__name__)


@app.before_request
def before_request():
    """Conect to the datebase before each request"""
    db = models.DATABASE
    db.connect()


@app.after_request
def after_reqest(response):
    """Close the datebase after each request"""
    models.DATABASE.close()
    return response

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/questions', methods=('GET', 'POST'))
def questions_import():
    """Html import page for import applicants """
    if request.method == "POST":
        file = request.form['questions']
        list_file = file[1:-1]
        new_file = json.loads(list_file)
        get_json = json.dumps(new_file)
        models.Questions.add(questionid=json.loads(get_json.lower())['id'], userid=1000,
                             question=json.loads(get_json.lower())['question'],
                             answer=json.loads(get_json.lower())['answer'])
    return render_template('questionimported.html')


@app.route('/applicant', methods=('GET', 'POST'))
def applicant_import():
    """Html import page for import applicants """
    if request.method == "POST":
        file = request.form['applicants']
        new_file = json.loads(file)
        get_json = json.dumps(new_file)
        applicants = GetApplicants.qualified(json.loads(get_json))
        return json.dumps(applicants)
    return render_template('applicantimport.html')


@app.route('/file/get_applicants', methods=['GET'])
def get_apps():
    """Get applicants from a json file"""
    jsonFile = open('applicants.json', )
    file = json.load(jsonFile)
    applicants = GetApplicants.qualified(file)
    jsonFile.close()
    return json.dumps(applicants)
