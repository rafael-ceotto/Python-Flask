from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField
from ..models.anuncio import Anuncio
from ..models.categoria import Categoria
from ..database import db


class AnuncioCategoria(Model):
    anuncio = ForeignKeyField(Anuncio, backref='categorias')
    categoria = ForeignKeyField(Categoria, backref='anuncios')
    ativo = BooleanField()
    data_cadastro = DateTimeField()
    data_exclusao = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'anuncios_categorias'
