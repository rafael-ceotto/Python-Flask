from peewee import Model, CharField, DateTimeField
from app.database import db

class Usuario(Model):
    login = CharField(45)
    senha = CharField(140)
    senha_hash=CharField(140)
    data_criacao = DateTimeField()
    data_exclusao = DateTimeField(null=True)
    class Meta:
        database = db
        table_name = 'usuarios'