from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime, timezone

from app.models.categoria import Categoria

categoria_dashboard_route = Blueprint('categoria_dashboard', __name__, url_prefix='/categoria')


@categoria_dashboard_route.route("/")
def index():
    return render_template("dashboard/categorias.html")


@categoria_dashboard_route.route('/todos')
def todas_categorias():
    categorias = Categoria.select()
    return render_template('dashboard/categorias_result.html', categorias=categorias)


@categoria_dashboard_route.route('/adicionar_formulario')
def adicionar_formulario():
    return render_template('dashboard/categorias_form.html')


@categoria_dashboard_route.route("/editar_formulario/<int:categoria_id>")
def editar_formulario(categoria_id):
    categoria = Categoria.get_by_id(categoria_id)
    return render_template("dashboard/categorias_form.html", categoria=categoria)


@categoria_dashboard_route.route("/adicionar_categoria", methods=["POST"])
def adicionar_categoria():
    categoria = request.json
    nova_categoria = Categoria.create(imagem=categoria["imagem"],
                                      nome=categoria["nome"],
                                      pai_id=categoria["pai_id"] if categoria["pai_id"] else None,
                                      descricao=categoria["descricao"],
                                      ativo=True if categoria["ativo"] == "on" else False,
                                      data_criacao=datetime.now(timezone.utc),
                                      data_edicao=datetime.now(timezone.utc))

    return render_template("dashboard/categorias_item.html", categoria=nova_categoria)


@categoria_dashboard_route.route("/deletar_categoria/<int:categoria_id>", methods=["DELETE"])
def deletar_categorias(categoria_id):
    Categoria.delete_by_id(categoria_id)
    return render_template("dashboard/categorias_result.html", categorias=Categoria.select())


@categoria_dashboard_route.route("/editar_categoria/<int:categoria_id>", methods=["PUT"])
def editar_categoria(categoria_id):
    categoria = request.json
    atualizar_categoria = Categoria.update(imagem=categoria["imagem"],
                                           nome=categoria["nome"],
                                           pai_id=categoria["pai_id"] if categoria["pai_id"] else None,
                                           descricao=categoria["descricao"],
                                           ativo=True if categoria["ativo"] == "on" else False).where(Categoria.id == categoria_id).execute()
    return render_template("dashboard/categorias_item.html", categoria=categoria)
