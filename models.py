from peewee import IntegerField, TextField, Model, SqliteDatabase

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


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Questions], safe=True)


def view_all():
    query = Questions.select().dicts()

    for items in query:
        print(items)


if __name__ == '__main__':
    initialize()
    # Questions.add(questionid=1, userid=1000, question="Do you have a car", answer="yes")
    view_all()
