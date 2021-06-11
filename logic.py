import json
import models

class GetApplicants:
    @staticmethod
    def qualified(file):
        ifTrue = True
        good_applicants = []
        for applicants in file:
            for question in applicants['questions']:
                question_field = models.Questions.get(models.Questions.questionid == question['id']).answer
                if question_field.lower().strip() == question['answer'].lower().strip():
                    ifTrue = True
                else:
                    ifTrue = False
            if ifTrue:
                good_applicants.append(applicants)
        return good_applicants
