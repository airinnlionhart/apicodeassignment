<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
=======
from flask import Flask, render_template, request, jsonify, redirect, url_for
>>>>>>> Dev
import models
import json
from logic import GetApplicants
from os import listdir
from os.path import isfile, join
<<<<<<< HEAD
from random import randint
=======

>>>>>>> Dev

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
<<<<<<< HEAD
        questionid = items['Id']
        question = items['Question']
        answer = items['Answer']
        models.Questions.add(questionid=questionid, userid=1000,
                             question=question,
                             answer=answer)
=======
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
>>>>>>> Dev

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
<<<<<<< HEAD
            models.Questions.add(questionid=item['Id'], userid=1000,
                             question=item['Question'],
                             answer=item['Answer'])
=======
            try:
                models.Questions.add(questionid=item['Id'], userid=1000,
                                     question=item['Question'],
                                     answer=item['Answer'])
            except:
                models.Questions.add(questionid=item['id'], userid=1000,
                                     question=item['question'],
                                     answer=item['answer'])
        return redirect(url_for('index'))
>>>>>>> Dev
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


<<<<<<< HEAD
@app.route('/file/get_applicants', methods=['GET'])
def get_apps():
    """Get applicants from a json file"""
    if models.Applicants.table_exists():
        pass
    else:
        models.DATABASE.create_tables([models.Applicants], safe=True)
    if models.AppQuestions.table_exists():
        pass
    else:
        models.DATABASE.create_tables([models.AppQuestions], safe=True)
    jsonFile = open('applicants.json', )
    file = json.load(jsonFile)
    for applicant in file:
        appid = randint(2000, 100000)
        try:
            models.Applicants.add(appid=appid, name=applicant['Name'])
            for questions in applicant['Questions']:
                models.AppQuestions.add(appid=appid, questionid=questions['Id'], answer=questions['Answer'])
                GetApplicants.qualified_applicants(appid)

        except:
            """For the off chance that random number comes up with the same number"""
            appid = randint(2000, 100000)
            models.Applicants.add(appid=appid, name=applicant['Name'])
            for questions in applicant['Questions']:
                models.AppQuestions.add(appid=appid, questionid=questions['Id'], answer=questions['Answer'])
                GetApplicants.qualified_applicants(appid)

    qualified_applicants = models.Applicants.select().dicts().where(models.Applicants.qualified == True)

    jsonFile.close()
    return jsonify(str([items for items in qualified_applicants]))


=======
>>>>>>> Dev
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
<<<<<<< HEAD
    print(json.loads(all_questions))
=======
>>>>>>> Dev
    for question in json.loads(all_questions):
        try:
            models.Questions.add(questionid=question['Id'], userid=10000, question=question['Question'],
                                 answer=question['Answer'])
        except:
<<<<<<< HEAD
            pass
=======
            models.Questions.add(questionid=question['id'], userid=10000, question=question['question'],
                                 answer=question['answer'])
>>>>>>> Dev

    for files in only_app_files:
        jsonFile = open('applicantfile/' + files, )
        file = json.load(jsonFile)
        applicants = GetApplicants.qualified(file)
        good_applicant.append(applicants)

    return json.dumps(good_applicant)
<<<<<<< HEAD
=======

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
>>>>>>> Dev
