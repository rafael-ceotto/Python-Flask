from flask_bootstrap import Bootstrap5
from flask import Flask

from app.models.contato import Contato
from app.models.newsletter import Newsletter

# Rotas do Website
from .routes import main_route
from .routes.buscar import buscar_route
from .routes.newsletter import newsletter_route
from .routes.contato import contato_route


# Rotas do Dashboard
from .routes.dashboard import dashboard_route
from .routes.dashboard.cliente import cliente_dashboard_route
from .routes.dashboard.anuncio import anuncio_dashboard_route
from .routes.dashboard.produto import produto_dashboard_route
from .routes.dashboard.regiao import regiao_dashboard_route
from .routes.dashboard.categoria import categoria_dashboard_route
from .routes.dashboard.options import options_dashboard_route

# Banco de Dados
from .database import db
from .models.cliente import Cliente
from .models.produto import Produto
from .models.anuncio import Anuncio
from .models.regiao import Regiao
from .models.categoria import Categoria
from .models.anuncio_categoria import AnuncioCategoria
from .models.anuncio_regiao import AnuncioRegiao


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'MK+HoWb6y7tq26IdRxaVQPLfl9rZ84t2YEEzm2rGKqEGVJO3Egpk5yBBJn25vD++/yx9Ve2r8t37j1u5IN3zJw=='
    app.config["JWT_SECRET_KEY"] = '8UAbSFFYCtplWL0fOJohYa2KedcBOAr0C1EujAFWFhMO4POoK5gg84eDmMW/tNL4vRJzwwk65DAIy9VO2evdJg=='
    app.config['JWT_TOKEN_LOCATION'] = ['headers']

    bootstrap = Bootstrap5(app)

    db.connect()
    db.create_tables([Cliente, Produto, Anuncio, Regiao,
                     Categoria, AnuncioCategoria, AnuncioRegiao, Contato, Newsletter])
    db.close()

    # Registro de rotas
    app.register_blueprint(main_route)
    app.register_blueprint(buscar_route, url_prefix="/buscar")
    app.register_blueprint(newsletter_route, url_prefix="/newsletter")

    app.register_blueprint(dashboard_route, url_prefix="/dashboard")
    app.register_blueprint(cliente_dashboard_route,
                           url_prefix="/dashboard/clientes")
    app.register_blueprint(anuncio_dashboard_route,
                           url_prefix="/dashboard/anuncios")
    app.register_blueprint(produto_dashboard_route,
                           url_prefix="/dashboard/produtos")
    app.register_blueprint(regiao_dashboard_route,
                           url_prefix="/dashboard/regioes")
    app.register_blueprint(categoria_dashboard_route,
                           url_prefix="/dashboard/categorias")
    app.register_blueprint(options_dashboard_route,
                           url_prefix="/dashboard/options")

    app.register_blueprint(contato_route, url_prefix="/contato")

    return app


