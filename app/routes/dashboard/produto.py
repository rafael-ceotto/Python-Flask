from flask import Blueprint, render_template, request, redirect, url_for

from app.models.produto import Produto

produto_dashboard_route = Blueprint('produto', __name__, url_prefix='/produto')


@produto_dashboard_route.route('/')
def listar_produtos():
    produtos = Produto.select()
    return render_template('dashboard/produtos.html', produtos=produtos)