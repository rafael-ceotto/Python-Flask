from peewee import Model, CharField, DateTimeField
from ..database import db

class Newsletter(Model):
    email = CharField(140)
    data_criacao = DateTimeField()
    data_exclusao = DateTimeField(null=True)
    class Meta:
        database = db
        table_name = "newsletter"
