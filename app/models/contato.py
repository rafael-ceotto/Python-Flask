from peewee import Model, CharField, DateTimeField
from ..database import db


class Contato(Model):
    nome = CharField(45)
    email = CharField(160)
    telefone = CharField(25)
    assunto = CharField(25)
    mensagem = CharField(1000)
    data_criacao = DateTimeField()

    class Meta:
        database = db
        table_name = 'contatos'
