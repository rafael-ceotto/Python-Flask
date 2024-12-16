from flask import Blueprint, render_template, request, url_for
from datetime import datetime

from ...models.cliente import Cliente

cliente_dashboard_route = Blueprint("cliente_dashboard", __name__)


@cliente_dashboard_route.route("/")
def index():
    return render_template("dashboard/clientes.html")


@cliente_dashboard_route.route("/todos")
def todos_clientes():
    clientes = Cliente.select()
    return render_template("dashboard/clientes_result.html", clientes=clientes)


@cliente_dashboard_route.route("/formulario")
def form_cliente():
    return render_template("dashboard/clientes_form.html")


@cliente_dashboard_route.route("/novo", methods=["POST"])
def inserir_cliente():
    cliente = request.json
    novo_cliente = Cliente.create(
        nome=cliente["nome"],
        email=cliente["email"],
        telefone=cliente["telefone"],
        endereco=cliente["endereco"],
        cidade=cliente["cidade"],
        estado=cliente["estado"],
        cep=cliente["cep"],
        sexo=cliente["sexo"],
        data_nascimento=cliente["data_nascimento"],
        data_cadastro=datetime.now(),
        data_edicao=datetime.now(),
        ativo=True,
    )
    
    return render_template("dashboard/clientes_item.html", cliente=novo_cliente)


@cliente_dashboard_route.route("/editar/<int:cliente_id>")
def editar_cliente(cliente_id):
    
    cliente = Cliente.get_by_id(cliente_id)
    
    return render_template("dashboard/clientes_form.html", cliente=cliente)

@cliente_dashboard_route.route("/atualizar/<int:cliente_id>", methods=["PUT"])
def atualizar_cliente(cliente_id):
    cliente = request.json
    
    cliente_atualizado = Cliente.get_by_id(cliente_id)
    cliente_atualizado.nome=cliente["nome"]
    cliente_atualizado.email=cliente["email"]
    cliente_atualizado.telefone=cliente["telefone"]
    cliente_atualizado.endereco=cliente["endereco"]
    cliente_atualizado.cidade=cliente["cidade"]
    cliente_atualizado.estado=cliente["estado"]
    cliente_atualizado.cep=cliente["cep"]
    cliente_atualizado.sexo=cliente["sexo"]
    cliente_atualizado.data_nascimento=cliente["data_nascimento"]
    cliente_atualizado.data_edicao=datetime.now()
    cliente_atualizado.save()
    cliente["id"] = cliente_id
    return render_template("dashboard/clientes_item.html", cliente=cliente)


@cliente_dashboard_route.route("/excluir/<int:cliente_id>", methods=["DELETE"])
def excluir_cliente(cliente_id):

    Cliente.get_by_id(cliente_id).delete_instance()
    
    return render_template("dashboard/clientes_result.html", clientes = Cliente.select())
