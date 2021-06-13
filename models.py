from peewee import IntegerField, TextField, Model, SqliteDatabase, BooleanField
import json

DATABASE = SqliteDatabase('notmongo.db')


class Questions(Model):
    questionid = IntegerField(unique=True, null=True)
    userid = IntegerField(null=True)
    question = TextField(null=True)
    answer = TextField(null=True)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, questionid, userid, question, answer):
        with DATABASE.transaction():
            cls.create(questionid=questionid, userid=userid, question=question, answer=answer)


class Applicants(Model):
    appid = IntegerField(unique=True, null=True)
    name = TextField(null=True)
    qualified = BooleanField(default=True)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, appid, name):
        with DATABASE.transaction():
            cls.create(appid=appid, name=name)


class AppQuestions(Model):
    appid = IntegerField(null=True)
    questionid = IntegerField(null=True)
    answer = TextField(null=True)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, appid, questionid, answer):
        with DATABASE.transaction():
            cls.create(appid=appid, questionid=questionid, answer=answer)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Questions], safe=True)
    DATABASE.create_tables([Applicants], safe=True)
    DATABASE.create_tables([AppQuestions], safe=True)


def view_all():
    query = Questions.select().dicts()
    query1 = AppQuestions.select().dicts()
    query2 = Applicants.select().dicts()

    for items in query:
        print(items)

    for items in query1:
        print(items)

    for items in query2:
        print(items)



if __name__ == '__main__':
    initialize()
    # Questions.add(questionid=1, userid=1000, question="Do you have a car", answer="yes")
    # qry = Questions.delete().where(Questions.id > 0).execute()
    # qry = AppQuestions.delete().where(AppQuestions.id >= 0).execute()
    # qry = Applicants.delete().where(Applicants.id >= 0).execute()
    view_all()
