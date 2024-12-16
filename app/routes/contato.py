from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from app.models.contato import Contato

contato_route = Blueprint('contato', __name__)


@contato_route.route('/register', methods=['POST'])
def salvar_contato():
    formData = request.json
    contato_criado = Contato.create(
        nome=formData["nome"],
        email=formData["email"],
        telefone=formData["telefone"],
        assunto=formData["assunto"],
        mensagem=formData["mensagem"],
        data_criacao=datetime.utcnow()
    )
    return jsonify({"status": 200, "message": "Enviado com sucesso"})
