from flask import Flask, render_template, request, jsonify, redirect, url_for
import models
import json
from logic import GetApplicants
from os import listdir
from os.path import isfile, join


Debug = True

app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to the database before each request"""
    db = models.DATABASE
    db.connect()


@app.after_request
def after_request(response):
    """Close the database after each request"""
    models.DATABASE.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_question', methods=("GET", "POST"))
def add():
    """route to post questions"""
    for items in json.loads(json.dumps(request.get_json())):
        try:
            questionid = items['Id']
            question = items['Question']
            answer = items['Answer']
            models.Questions.add(questionid=questionid, userid=1000,
                                 question=question,
                                 answer=answer)
        except:
            questionid = items['id']
            question = items['question']
            answer = items['answer']
            models.Questions.add(questionid=questionid, userid=1000,
                                 question=question,
                                 answer=answer)

    return "added questions"


@app.route('/get_qualified', methods=("GET", "POST"))
def get_qualified():
    """route to post and get back qualified applicants"""

    new_file = request.get_json()[:]
    get_json = json.dumps(new_file)
    applicants = GetApplicants.qualified(json.loads(get_json))
    return json.dumps(applicants)


@app.route('/questions', methods=('GET', 'POST'))
def questions_import():
    """Html import page for import applicants """
    if request.method == "POST":
        file = request.form['questions']
        for item in json.loads(file):
            try:
                models.Questions.add(questionid=item['Id'], userid=1000,
                                     question=item['Question'],
                                     answer=item['Answer'])
            except:
                models.Questions.add(questionid=item['id'], userid=1000,
                                     question=item['question'],
                                     answer=item['answer'])
        return redirect(url_for('index'))
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


@app.route('/infolder', methods=['GET'])
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
            models.Questions.add(questionid=question['Id'], userid=10000, question=question['Question'],
                                 answer=question['Answer'])
        except:
            models.Questions.add(questionid=question['id'], userid=10000, question=question['question'],
                                 answer=question['answer'])

    for files in only_app_files:
        jsonFile = open('applicantfile/' + files, )
        file = json.load(jsonFile)
        applicants = GetApplicants.qualified(file)
        good_applicant.append(applicants)

    return json.dumps(good_applicant)

@app.route('/clear')
def clear():
    models.Questions.delete().where(models.Questions.id > 0).execute()
    return render_template('index.html')

@app.errorhandler(400)
def page_400(e):
    # note that we set the 400 status explicitly
    return "This is not format it was looking for please check values and try again make sure " \
           "Key are capitalized and that it in a list" \
        , 400


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Sorry this page can not be found ", 404


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 400 status explicitly
    return "You might have some incorrect values that we don't accept please look over what your sending and try again", 400
