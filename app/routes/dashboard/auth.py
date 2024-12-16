from flask import Blueprint, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from app.models.usuario import Usuario
auth_dashboard = Blueprint("auth", __name__)

@auth_dashboard.route("/login", methods=["POST"])
def login():
    form = request.json
    existing = Usuario.select().where()
    
    
    