from peewee import Model, CharField, DateField, BooleanField, DateTimeField
from ..database import db


class Cliente(Model):
    nome = CharField(140)
    email = CharField(240)
    telefone = CharField(20)
    endereco = CharField(500, null=True)
    cidade = CharField(45, null=True)
    estado = CharField(25, null=True)
    cep = CharField(10, null=True)
    sexo = CharField(1, null=True)
    company_name = CharField(140, null=True)
    company_logo = CharField(45, null=True)
    ativo = BooleanField()
    data_nascimento = DateField(null=True)
    data_cadastro = DateTimeField()
    data_edicao = DateTimeField()
    data_exclusao = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = "clientes"
