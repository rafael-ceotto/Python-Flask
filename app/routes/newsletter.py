from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from app.models.newsletter import Newsletter


newsletter_route = Blueprint('newsletter', __name__)


@newsletter_route.route("/subscribe", methods=['POST'])
def inscrever():
    formData = request.json
    Newsletter.create(
        email=formData["email"],
        data_criacao=datetime.utcnow()
    )
    return jsonify({"status": 200, "message": "Enviado com sucesso"})
