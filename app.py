from flask import Flask, redirect, render_template, url_for, request
import models
import json
from logic import GetApplicants
from os import listdir
from os.path import isfile, join



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
        models.Questions.add(questionid=json.loads(get_json.lower())['id'], userid=10000,
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


@app.route('/files', methods=['GET'])
def form_file():
    if models.Questions.table_exists():
        pass
    else:
        models.DATABASE.create_tables([models.Questions], safe=True)

    only_app_files = [f for f in listdir('applicantfile') if isfile(join('applicantfile', f))]
    questions_json = []
    good_applicant = []

    only_qs_files = [f for f in listdir('questionfile') if isfile(join('questionfile', f))]
    for files in only_qs_files:
        json_Q_File = open('questionfile/' + files, )
        file = json.load(json_Q_File)
        questions_json.append(file)

    all_questions = json.dumps(questions_json[0])
    for question in json.loads(all_questions):
            try:
                models.Questions.add(questionid=question['id'], userid=10000, question=question['question'],
                                     answer=question['answer'])
            except:
                pass

    for files in only_app_files:
        jsonFile = open('applicantfile/' + files, )
        file = json.load(jsonFile)
        applicants = GetApplicants.qualified(file)
        good_applicant.append(applicants)


    return json.dumps(good_applicant)
