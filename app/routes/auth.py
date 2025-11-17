from flask import Blueprint, request, jsonify
from app.services.user_service import cadastrar_usuario, autenticar_usuario, listar_usuarios


auth_bp = Blueprint('auth', __name__, url_prefix='/api')


@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    """Endpoint de login de usuário"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response, 200
    
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    email = data.get('email')
    senha = data.get('senha')
    
    if not email or not senha:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400
    
    resultado = autenticar_usuario(email, senha)
    
    if resultado['sucesso']:
        return jsonify({
            "mensagem": resultado['mensagem'],
            "token": resultado['token'],
            "usuario": resultado['usuario']
        }), 200
    else:
        return jsonify({"erro": resultado['mensagem']}), 401


@auth_bp.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    """Endpoint de cadastro de novo usuário"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        return response, 200
    
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    data_nasc = data.get('data_nasc')
    idade = data.get('idade')
    sexo = data.get('sexo')
    
    if not email or not senha:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400
    
    resultado = cadastrar_usuario(nome, email, senha, data_nasc, idade, sexo)
    
    if resultado['sucesso']:
        return jsonify({"mensagem": resultado['mensagem']}), 201
    else:
        return jsonify({"erro": resultado['mensagem']}), 400


@auth_bp.route('/users', methods=['GET', 'OPTIONS'])
def get_users():
    """Endpoint para listar todos os usuários (sem senhas)"""
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 200
    
    usuarios = listar_usuarios()
    return jsonify(usuarios), 200
