from peewee import Model, CharField, DateTimeField, BooleanField, ForeignKeyField
from ..models.cliente import Cliente
from ..models.produto import Produto
from ..database import db


class Anuncio(Model):
    cliente = ForeignKeyField(Cliente, backref='anuncios')
    produto = ForeignKeyField(Produto, backref='anuncios')
    imagem = CharField(50, null=True)
    descricao = CharField(140)
    telefone = CharField(20)
    email = CharField(240)
    website = CharField(240, null=True)
    instagram = CharField(240, null=True)
    whatsapp = CharField(240, null=True)
    tiktok = CharField(240, null=True)
    ativo = BooleanField()
    data_criacao = DateTimeField()
    data_edicao = DateTimeField()
    data_exclusao = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'anuncios'
