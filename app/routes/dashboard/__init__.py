from flask import Blueprint, render_template, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

from ...models.anuncio import Anuncio
dashboard_route = Blueprint('dashboard', __name__)

@dashboard_route.route('/')
#@jwt_required()
def index():
    return render_template('dashboard/home.html', anuncios = Anuncio )
