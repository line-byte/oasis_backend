import os
import json
import jwt
import bcrypt
from datetime import datetime, timedelta


USERS_FILE = "data/users.json"


def carregar_usuarios():
    """Carrega usuários do arquivo JSON"""
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []


def salvar_usuarios(usuarios):
    """Salva usuários no arquivo JSON"""
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, ensure_ascii=False, indent=4)


def gerar_id_usuario(usuarios):
    """Gera um ID único para novo usuário"""
    if not usuarios:
        return 1
    return max(u.get('id', 0) for u in usuarios) + 1


def buscar_usuario_por_email(email):
    """Busca um usuário pelo email"""
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario.get('email') == email:
            return usuario
    return None


def cadastrar_usuario(nome, email, senha, data_nasc=None, idade=None, sexo=None):
    """Cadastra um novo usuário"""
    usuarios = carregar_usuarios()
    
    # Verifica se email já existe
    if buscar_usuario_por_email(email):
        return {"sucesso": False, "mensagem": "Email já cadastrado"}
    
    # Gera hash da senha
    hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Cria novo usuário
    novo_usuario = {
        "id": gerar_id_usuario(usuarios),
        "nome": nome,
        "email": email,
        "senha": hash_senha,
        "idade": idade,
        "data_nascimento": data_nasc,
        "sexo": sexo,
        "data_criacao": str(datetime.now().date())
    }
    
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    
    return {"sucesso": True, "mensagem": "Usuário cadastrado com sucesso"}


def autenticar_usuario(email, senha):
    """Autentica um usuário e retorna token JWT"""
    usuario = buscar_usuario_por_email(email)
    
    if not usuario:
        return {"sucesso": False, "mensagem": "Credenciais inválidas"}
    
    senha_hash = usuario.get('senha')
    if not senha_hash:
        return {"sucesso": False, "mensagem": "Erro ao verificar credenciais"}
    
    # Verifica senha
    if not bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
        return {"sucesso": False, "mensagem": "Credenciais inválidas"}
    
    # Gera token JWT
    SECRET_KEY = os.getenv('SECRET_KEY') or 'changeme'
    token = jwt.encode({
        'user_id': usuario.get('id'),
        'email': usuario.get('email'),
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')
    
    return {
        "sucesso": True,
        "mensagem": "Login realizado com sucesso",
        "token": token,
        "usuario": {
            "id": usuario.get('id'),
            "nome": usuario.get('nome'),
            "email": usuario.get('email')
        }
    }


def listar_usuarios():
    """Retorna lista de usuários (sem senhas)"""
    usuarios = carregar_usuarios()
    usuarios_sem_senha = []
    
    for usuario in usuarios:
        usuario_limpo = {k: v for k, v in usuario.items() if k != 'senha'}
        usuarios_sem_senha.append(usuario_limpo)
    
    return usuarios_sem_senha
