import urllib.parse
import urllib.response
from flask import Blueprint, render_template, request, url_for
from ..models.anuncio import Anuncio
from ..models.regiao import Regiao
from ..models.categoria import Categoria
from ..models.anuncio_categoria import AnuncioCategoria
from ..models.anuncio_regiao import AnuncioRegiao
from ..models.cliente import Cliente
from peewee import fn
import urllib

buscar_route = Blueprint("buscar", __name__)

@buscar_route.route("/")
def index():
    params = request.args
    q = params.get("q")
    cidades = params.get('cidades')
    categorias = params.get("categorias")
    anuncios = (Anuncio.select()
                .join(AnuncioCategoria)
                .join(Categoria)
                .switch(Anuncio)
                .join(AnuncioRegiao)
                .join(Regiao))

    if q != None and q != "":
        anuncios = Anuncio.select().where(Anuncio.descricao.contains(q))

    anuncios = filtar_resultado(anuncios, categorias, cidades)
    

    return render_template(
        "busca.html",
        query=q,
        anuncios=anuncios,
        obter_regioes=obter_regioes,
        categorias=lista_categorias(),
        regioes=lista_regioes(),
    )
def coma(value):
    return value.replace('  ',', ')

def filtar_resultado(anuncios, categorias, cidades):

    print(cidades)

    if categorias != None and categorias != "":
        anuncios = anuncios.where(Categoria.nome.in_(categorias.split(",")))

    if cidades != None and cidades != "":
        query = map(coma, cidades.split(','))
        anuncios = anuncios.where(Regiao.nome.in_(list(query)))
    
    print(list(anuncios))
    return anuncios

def obter_regiao(regiao_id):
    return Regiao.get_by_id(regiao_id)

def obter_regioes(anuncio_id):
    regioes = []
    for regiao in Anuncio.get_by_id(anuncio_id).regioes:
        regioes.append(obter_regiao(regiao.regiao_id).nome)

    return len(regioes) > 0 and ", ".join(regioes) or "Não informado"

def lista_categorias():
    return Categoria.select().join(AnuncioCategoria).distinct()

def lista_regioes():
    return Regiao.select().join(AnuncioRegiao).distinct()
