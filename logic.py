import models


class GetApplicants:
    @staticmethod
    def qualified(file):
        ifTrue = True
        good_applicants = []
        for applicants in file:
            try:
                for question in applicants['Questions']:
                    try:
                        question_field = models.Questions.get(models.Questions.questionid == question['Id']).answer
                    except:
                        print('No Applicants match')
                if question_field.lower().strip() == question['Answer'].lower().strip():
                    ifTrue = True
                else:
                    ifTrue = False
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
            if ifTrue:
                good_applicants.append(applicants)
        return good_applicants

