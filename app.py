import os
import jwt
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import bcrypt

load_dotenv()

"""
    Esta branch pertence ao desenvolvedor: Abraão

    LISTA DE ALTERAÇÕES:
    - Alt 1,
    - Alt 2,
    - Alt 3,
    - Alt 4,
    - ...
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
    with open("data/habitos.json", "r", encoding="utf-8") as file:
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
        
        hash_armazenado = usuario_encontrado.get('senha')

        if not hash_armazenado:
            return jsonify({"Erro": "Senha não cadastrada..."}), 500
        
        if not bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado.encode('utf-8')):
            return jsonify({"Erro": "Credenciais inválidas!"}), 401

        SECRET_KEY = os.getenv('SECRET_KEY')
        token = jwt.encode({
            'user_id': usuario_encontrado.get('id'),
            'email': usuario_encontrado.get('email'),
            }, SECRET_KEY, algorithm='HS256')
        

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

@server.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response, 200

    data = request.get_json()
    if not data:
        return jsonify({"Erro": "Nenhum dado recebido!"}), 400
    
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    data_nasc = data.get('data_nasc')
    idade = data.get('idade')
    sexo = data.get('sexo')

    if not email or not senha:
        return jsonify({"Erro": "Campos obrigatórios estão vazios"}), 400
    
    try:
        with open("data/users.json", "r", encoding="utf-8") as file:
            users = json.load(file)

            hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

            new_user = {"nome": nome, "email": email, "senha": hash_senha, "idade": idade, "data_nascimento": data_nasc, "sexo": sexo}
            users.append(new_user)

        with open("data/users.json", "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=False, indent=4)

        return jsonify({"Message":"User registered successfully!"}), 201
    
    except FileNotFoundError:
        return jsonify({"Error": "Database file not found..."}), 404
    except json.JSONDecodeError:
        return jsonify({"Error": "Error reading users file..."}), 500   


if __name__ == "__main__":
    server.run()
    