from flask import Blueprint, render_template, redirect
from ..models.categoria import Categoria


main_route = Blueprint('main', __name__)

@main_route.route('/')
def index():
    categorias = Categoria.select().paginate(0,5)
    return render_template('home.html', categorias = categorias)

@main_route.route('/categorias')
def categorias():
    categorias = Categoria.select()
    return render_template('categoria.html', categorias = categorias)

@main_route.route('/faq')
def faq():
    return render_template('faq.html')

@main_route.route('/contato')
def contato():
    return render_template('contato.html')

@main_route.route('/politica-de-privacidade')
def politica_de_privacidade():
    return render_template('politica-de-privacidade.html')

@main_route.route('/whatsapp')
def whatsapp():
    return redirect('https://wa.me/13262136008?text=Olá%2C+vi+o+site+Brasil+na+Gringa+e+fiquei+interessado')