import models

class GetApplicants:
    @staticmethod
    def qualified(file):
        good_applicants = []
        number_of_questions = len(models.Questions.select().dicts())
        for applicants in file:
            try:
                print(len(applicants['Questions']))
                good_applicants.append(applicants)
                if number_of_questions != len(applicants['Questions']):
                    good_applicants.remove(applicants)
                else:
                    for question in applicants['Questions']:
                        question_field = models.Questions.get(models.Questions.questionid == question['Id']).answer
                        if question_field.lower().strip() != question['Answer'].lower().strip():
                            good_applicants.remove(applicants)
            except:
                print(len(applicants['questions']))
                good_applicants.append(applicants)
                if number_of_questions != len(applicants['questions']):
                    good_applicants.remove(applicants)
                else:
                    for question in applicants['questions']:
                        question_field = models.Questions.get(models.Questions.questionid == question['id']).answer
                        if question_field.lower().strip() != question['answer'].lower().strip():
                            good_applicants.remove(applicants)
        return good_applicants
