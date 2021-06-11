from peewee import IntegerField, TextField, Model, SqliteDatabase
import json

DATABASE = SqliteDatabase('notmongo.db')


class Questions(Model):
    questionid = IntegerField(null=True)
    userid = IntegerField(null=True)
    question = TextField(null=True)
    answer = TextField(null=True)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, questionid, userid, question, answer):
        with DATABASE.transaction():
            cls.create(questionid=questionid, userid=userid, question=question, answer=answer)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Questions], safe=True)


def view_all():
    query = Questions.select().dicts()
    for items in query:
        print(items)

def edit(id):
    Questions.update(questionid="3", answer=True).where(Questions.id == id).execute()


if __name__ == '__main__':
    initialize()
    # userid = 10000
    # questions = [{"Id": "01", "Question": "Do you have a car", "Answer": "Yes"}]
    # for items in questions:
    #     Questions.add(questionid=items['Id'], userid=userid, question=items["Question"], answer=items["Answer"])
    view_all()
