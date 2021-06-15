<<<<<<< HEAD
import json
=======
>>>>>>> Dev
import models


class GetApplicants:
    @staticmethod
    def qualified(file):
        ifTrue = True
        good_applicants = []
        for applicants in file:
<<<<<<< HEAD
            for question in applicants['Questions']:
                question_field = models.Questions.get(models.Questions.questionid == question['Id']).answer
=======
            try:
                for question in applicants['Questions']:
                    try:
                        question_field = models.Questions.get(models.Questions.questionid == question['Id']).answer
                    except:
                        print('No Applicants match')
>>>>>>> Dev
                if question_field.lower().strip() == question['Answer'].lower().strip():
                    ifTrue = True
                else:
                    ifTrue = False
<<<<<<< HEAD
=======
            except:
                for question in applicants['questions']:
                    try:
                        question_field = models.Questions.get(models.Questions.questionid == question['id']).answer
                    except:
                        print('No Applicants match')
                if question_field.lower().strip() == question['answer'].lower().strip():
                    ifTrue = True
                else:
                    ifTrue = False
>>>>>>> Dev
            if ifTrue:
                good_applicants.append(applicants)
        return good_applicants

<<<<<<< HEAD
    @staticmethod
    def qualified_applicants(appid):
        if models.Applicants.table_exists():
            pass
        else:
            models.DATABASE.create_tables([models.Applicants], safe=True)
        if models.AppQuestions.table_exists():
            pass
        else:
            models.DATABASE.create_tables([models.AppQuestions], safe=True)

        apps_questions = models.AppQuestions.select().dicts().where(models.AppQuestions.appid == appid)
        for answers in apps_questions:
            question_field = models.Questions.get(models.Questions.questionid == answers['questionid']).answer
            if str(question_field.lower().strip()) != str(answers['answer'].lower().strip()):
                models.Applicants.update(qualified=False).where(models.Applicants.appid == appid).execute()
            else:
                pass
        return "updated"
=======
>>>>>>> Dev
