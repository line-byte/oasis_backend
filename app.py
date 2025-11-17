import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

"""
    Oasis Backend - API REST
    
    Sistema modularizado com Blueprints para:
    - Autenticação de usuários (login/signup)
    - Gerenciamento de hábitos (CRUD completo)
"""


def create_app():
    """Factory para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configuração CORS
    CORS(app, resources={r"/api/*": {
        "origins": "*", 
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type"]
    }})
    
    # Configurações da aplicação
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'changeme')
    app.config['JSON_AS_ASCII'] = False
    
    # Registrar Blueprints
    from app.routes.auth import auth_bp
    from app.routes.habits import habits_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(habits_bp)
    
    # Rota raiz
    @app.route('/')
    def home():
        return {
            "mensagem": "Bem-vindo à API Oasis",
            "versao": "2.0",
            "endpoints": {
                "auth": "/api/login, /api/signup, /api/users",
                "habits": "/api/habits, /api/habits/<id>"
            }
        }
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
    