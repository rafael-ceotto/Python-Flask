from peewee import Model, CharField, DateTimeField, BooleanField, IntegerField

from ..database import db


class Categoria(Model):
    pai_id = IntegerField(null=True)
    imagem = CharField(50, null=True)
    nome = CharField(50)
    destacar = BooleanField()
    ativo = BooleanField()
    data_criacao = DateTimeField()
    data_exclusao = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'categorias'
