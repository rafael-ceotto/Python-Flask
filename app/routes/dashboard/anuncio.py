from flask import Blueprint, render_template, request, url_for

from ...models.anuncio import Anuncio

anuncio_dashboard_route = Blueprint("anuncio_dashboard", __name__)

@anuncio_dashboard_route.route("/")
def index():
    return render_template("dashboard/anuncios.html")

@anuncio_dashboard_route.route("/todos")
def todos_anuncios():
    anuncios = Anuncio.select()
    return render_template("dashboard/anuncios_result.html", anuncios=anuncios)


@anuncio_dashboard_route.route("/formulario_adicionar")
def formulario_adicionar():
    return render_template("dashboard/anuncios_form.html")

@anuncio_dashboard_route.route("/novo", methods=["POST"])   
def adicionar_cliente():
    return render_template("dashboard/anuncios_form.html")