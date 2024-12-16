from peewee import Model, CharField, FloatField, DateTimeField, BooleanField
from ..database import db


class Produto(Model):
    nome = CharField(140)
    preco = FloatField()
    ativo = BooleanField()
    data_cadastro = DateTimeField()
    data_edicao = DateTimeField()
    data_exclusao = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'produtos'
