from peewee import Model, CharField, IntegerField,DateTimeField
from ..database import db

class Regiao(Model):
    pai_id = IntegerField(null=True)
    nome = CharField(140)
    latlong = CharField(255, null=True)
    data_criacao = DateTimeField()
    data_exclusao = DateTimeField(null = True)
    
    class Meta:
        database = db
        table_name = 'regioes'