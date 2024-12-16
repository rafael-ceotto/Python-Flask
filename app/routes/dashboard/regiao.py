from flask import Blueprint, render_template, request, url_for
from datetime import datetime, timezone
from ...models.regiao import Regiao

regiao_dashboard_route = Blueprint("regiao_dashboard", __name__)


@regiao_dashboard_route.route("/")
def index():
    return render_template("dashboard/regioes.html")


@regiao_dashboard_route.route("/search")
def search():
    nome = request.args.get('nome')
    regioes = Regiao.select().where(Regiao.nome.contains(nome))
    return render_template("dashboard/regioes_result.html", regioes=regioes)


@regiao_dashboard_route.route("/todos")
def todas_regioes():
    regioes = Regiao.select().where(Regiao.data_exclusao.is_null(True))
    return render_template("dashboard/regioes_result.html", regioes=regioes)


@regiao_dashboard_route.route("/adicionar_formulario")
def adicionar_formulario():
    return render_template("dashboard/regioes_form.html")


@regiao_dashboard_route.route("/editar_formulario/<int:regiao_id>")
def editar_formulario(regiao_id):
    regiao = Regiao.get_by_id(regiao_id)
    return render_template("dashboard/regioes_form.html", regiao=regiao)


@regiao_dashboard_route.route("/editar_regiao/<int:regiao_id>", methods=["PUT"])
def editar_regiao(regiao_id):
    regiao = request.json
    atualizar_regiao = Regiao.update(pai_id= None,
                                     nome=regiao["nome"],
                                     latlong = regiao["latlong"] if regiao["latlong"] else None).where(Regiao.id == regiao_id).execute()
    return render_template("dashboard/regioes_item.html", regiao=regiao)

@regiao_dashboard_route.route("/adicionar_regiao", methods=["POST"])
def adicionar_regiao():
    regiao = request.json
    nova_regiao = Regiao.create(pai_id= None,
                                     nome=regiao["nome"],
                                     latlong = regiao["latlong"] if regiao["latlong"] else None,
                                     data_criacao = datetime.now(timezone.utc))
    return render_template("dashboard/regioes_item.html", regiao=nova_regiao)

@regiao_dashboard_route.route("/deletar_regiao/<int:regiao_id>", methods=["DELETE"])
def deletar_regiao(regiao_id):
    Regiao.update(data_exclusao = datetime.now(timezone.utc)).where(Regiao.id == regiao_id).execute()
    regioes = Regiao.select().where(Regiao.data_exclusao == None)
    return render_template("dashboard/regioes_result.html", regioes = regioes)

