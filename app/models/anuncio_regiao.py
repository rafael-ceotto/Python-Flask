from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField
from .anuncio import Anuncio
from .regiao import Regiao
from ..database import db


class AnuncioRegiao(Model):
    anuncio = ForeignKeyField(Anuncio, backref='regioes')
    regiao = ForeignKeyField(Regiao, backref='anuncios')
    ativo = BooleanField()
    data_cadastro = DateTimeField()
    data_exclusao = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'anuncios_regioes'
