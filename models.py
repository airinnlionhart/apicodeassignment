from peewee import IntegerField, TextField, Model, SqliteDatabase

DATABASE = SqliteDatabase('notmongo.db')


class Questions(Model):
    questionId = IntegerField(primary_key=True)
    userId = IntegerField(null=True)
    question = TextField(null=False)
    answer = TextField(null=False)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, question, answer):
        with DATABASE.transaction():
            cls.create(question=question, answer=answer)

    @classmethod
    def add_user(cls, userId):
        with DATABASE.transaction():
            cls.create(userId=userId)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Questions], safe=True)

def view_all():
    query = Questions.select().dicts()
    for items in query:
        print(items)


