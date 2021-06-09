from peewee import IntegerField, TextField, Model, SqliteDatabase
import json

DATABASE = SqliteDatabase('notmongo.db')


class Questions(Model):
    questionId = IntegerField(primary_key=True)
    userId = IntegerField(null=True)
    question = TextField(null=True)
    answer = TextField(null=True)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, userId, question, answer):
        with DATABASE.transaction():
            cls.create(userId=userId, question=question, answer=answer)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Questions], safe=True)


def view_all():
    query = Questions.select().dicts()
    for items in query:
        print(items)


if __name__ == '__main__':
    initialize()
    userId = 10000
    questions = [{"Question": "Do you have a car", "Answer": "Yes"}, {"Question": "Are you over 18", "Answer": "Yes"}]
    for items in questions:
        Questions.add(userId=userId, question=items["Question"], answer=items["Answer"])
    view_all()
