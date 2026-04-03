from flask import request, jsonify
from app import db
from models.user import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.json

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    # Buscar usuário
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    # Verificar senha
    if not bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({"error": "Senha incorreta"}), 401

    # Criar token JWT
    token = create_access_token(identity=user.id)

    return jsonify({"token": token})