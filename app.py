# Aqui importamos os módulos da nossa aplicação
import os
import jwt
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

load_dotenv()
"""
Se quiser importar um arquivo, basta seguir o padrão:

import pasta.arquivo

ou se quiser importar funções específicas, use:

from pasta.nome_arquivo import funcao(ou '*' para importar todas de uma vez)
"""

server = Flask(__name__)
CORS(server, resources={r"/*": {
    "origins": "*", 
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
    "allow_headers": ["Content-Type", "Authorization"],
    "expose_headers": ["Content-Type"]
}})

@server.route('/')
def response():
    return 'Hello, and welcome to my page.'

@server.route('/habits', methods=['GET', 'OPTIONS'])
def habits_data():
    with open("data/habits.json", "r", encoding="utf-8") as file:
        habits = json.load(file)
    return jsonify(habits)

@server.route('/users', methods=['GET', 'OPTIONS'])
def user_data():
    with open("data/users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    return jsonify(users)

@server.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response, 200
    
    data = request.get_json()
    if not data:
        return jsonify({"Erro": "Nenhum dado recebido!"}), 400
    
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return json({"Erro": "Email e senha são obrigatórios!"}), 400
    
    try:

        with open('data/users.json', 'r', encoding='utf-8') as dados_usuarios:
            usuarios = json.load(dados_usuarios)

        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.get('email') == email:
                usuario_encontrado = usuario
                break
        
        SECRET_KEY = os.getenv('SECRET_KEY')
        token = jwt.encode({
            'user_id': usuario_encontrado.get('id'),
            'email': usuario_encontrado.get('email'),
            }, SECRET_KEY, algorithm='HS256')
        
        if usuario_encontrado.get('senha') == senha:
            return jsonify({
            "Mensagem": "Login realizado com sucesso!",
            "token": token,
            "Usuário": {
                "email": usuario_encontrado.get('email'),
                "nome": usuario_encontrado.get('nome')
            }                
            }), 200
    
    except FileNotFoundError:
        return jsonify({"Erro": "Arquivo de usuários não encontrado!"}), 500
    except json.JSONDecodeError:
        return jsonify({"Erro": "Erro ao ler arquivo de usuários!"}), 500


if __name__ == "__main__":
    server.run()
    