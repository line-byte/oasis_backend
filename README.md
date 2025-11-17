# Oasis Backend - API REST

Sistema de gerenciamento de hábitos saudáveis com autenticação de usuários.

## 🏗️ Arquitetura

Sistema modularizado seguindo padrões REST com separação de responsabilidades:

```
oasis_backend/
├── app.py                 # Aplicação principal (Factory Pattern)
├── requirements.txt       # Dependências do projeto
├── .env                   # Variáveis de ambiente
├── app/
│   ├── __init__.py
│   ├── routes/           # Blueprints (rotas da API)
│   │   ├── __init__.py
│   │   ├── auth.py       # Rotas de autenticação
│   │   └── habits.py     # Rotas de hábitos
│   └── services/         # Lógica de negócio
│       ├── __init__.py
│       ├── user_service.py    # Serviços de usuários
│       └── habit_service.py   # Serviços de hábitos
└── data/
    ├── users.json        # Banco de dados de usuários
    └── habitos.json      # Banco de dados de hábitos
```

## 🚀 Endpoints da API

### Autenticação (`/api`)

- **POST** `/api/login` - Login de usuário
- **POST** `/api/signup` - Cadastro de novo usuário
- **GET** `/api/users` - Listar usuários

### Hábitos (`/api`)

- **GET** `/api/habits` - Listar todos os hábitos
- **GET** `/api/habits/<id>` - Buscar hábito específico
- **POST** `/api/habits` - Criar novo hábito
- **PUT** `/api/habits/<id>` - Atualizar hábito
- **DELETE** `/api/habits/<id>` - Excluir hábito

## 📦 Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv OasisVenv
   source OasisVenv/bin/activate  # Linux/Mac
   # ou
   OasisVenv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente (`.env`):
   ```
   SECRET_KEY=sua_chave_secreta_aqui
   ```

5. Execute a aplicação:
   ```bash
   python app.py
   ```

## 🔧 Tecnologias

- **Flask** - Framework web
- **Flask-CORS** - Gerenciamento de CORS
- **bcrypt** - Hash de senhas
- **PyJWT** - Autenticação JWT
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 👥 Equipe

- Abraão Filipi dos Santos - afs6@cesar.school
- Dilvanir Aline Alves Cabral de Melo - daacm@cesar.school
- Emanoel Alesandro da Silva - eas3@cesar.school
- Marcio Aureliano Pedro da Silva - maps@cesar.school
- Maria Larysse Yasmin Lira Pereira - mlylp@cesar.school (Líder)
- Pedro Pessôa de Albuquerque Neto - ppan@cesar.school
