import models

class GetApplicants:
    @staticmethod
    def qualified(file):
        """
        Grabs a json file of applicants and compare questions to answers and return only good applicants
        """
        good_applicants = []
        number_of_questions = len(models.Questions.select().dicts())
        for applicants in file:
            good_applicants.append(applicants)
            if number_of_questions != len(applicants['Questions']):
                good_applicants.remove(applicants)
            else:
                for question in applicants['Questions']:
                    question_field = models.Questions.get(models.Questions.questionid == question['Id']).answer
                    if question_field.lower().strip() != question['Answer'].lower().strip():
                        good_applicants.remove(applicants)
                        break
        return good_applicants
