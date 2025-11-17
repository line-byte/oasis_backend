# 🚀 Quick Start Guide - Oasis Backend

## ⚡ Início Rápido (5 minutos)

### 1. Ativar Ambiente Virtual
```bash
source OasisVenv/bin/activate  # Linux/Mac
# ou
OasisVenv\Scripts\activate  # Windows
```

### 2. Iniciar Servidor
```bash
python app.py
```

O servidor estará rodando em: `http://localhost:5000`

---

## 📋 Estrutura do Projeto

```
app/
├── routes/          # 🛣️ Blueprints (Rotas da API)
│   ├── auth.py      # Login, Signup, Users
│   └── habits.py    # CRUD de Hábitos
└── services/        # 🧩 Lógica de Negócio
    ├── user_service.py     # Autenticação, Cadastro
    └── habit_service.py    # Gerenciamento de Hábitos
```

---

## 🎯 Primeiros Testes

### 1. Verificar se API está online
```bash
curl http://localhost:5000
```

**Resposta esperada:**
```json
{
  "mensagem": "Bem-vindo à API Oasis",
  "versao": "2.0",
  "endpoints": {
    "auth": "/api/login, /api/signup, /api/users",
    "habits": "/api/habits, /api/habits/<id>"
  }
}
```

### 2. Cadastrar Usuário
```bash
curl -X POST http://localhost:5000/api/signup \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Teste User",
    "email": "teste@oasis.com",
    "senha": "senha123"
  }'
```

### 3. Fazer Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "teste@oasis.com",
    "senha": "senha123"
  }'
```

### 4. Criar Hábito
```bash
curl -X POST http://localhost:5000/api/habits \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Meditação",
    "tempo": "15",
    "user_id": 1
  }'
```

### 5. Listar Hábitos
```bash
curl http://localhost:5000/api/habits
```

---

## 🔧 Integração com Front-End

### Exemplo HTML + JavaScript

```html
<!DOCTYPE html>
<html>
<head>
    <title>Oasis - Teste</title>
</head>
<body>
    <h1>Teste API Oasis</h1>
    
    <!-- Formulário de Login -->
    <div>
        <h2>Login</h2>
        <input type="email" id="email" placeholder="Email">
        <input type="password" id="senha" placeholder="Senha">
        <button onclick="fazerLogin()">Login</button>
    </div>
    
    <!-- Lista de Hábitos -->
    <div>
        <h2>Meus Hábitos</h2>
        <button onclick="carregarHabitos()">Carregar</button>
        <div id="habitos"></div>
    </div>

    <script>
        const API_URL = 'http://localhost:5000/api';
        
        async function fazerLogin() {
            const email = document.getElementById('email').value;
            const senha = document.getElementById('senha').value;
            
            try {
                const response = await fetch(`${API_URL}/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, senha })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    localStorage.setItem('token', data.token);
                    localStorage.setItem('user', JSON.stringify(data.usuario));
                    alert('Login realizado com sucesso!');
                    carregarHabitos();
                } else {
                    alert('Erro: ' + data.erro);
                }
            } catch (error) {
                alert('Erro ao conectar: ' + error.message);
            }
        }
        
        async function carregarHabitos() {
            try {
                const response = await fetch(`${API_URL}/habits`);
                const habitos = await response.json();
                
                const container = document.getElementById('habitos');
                container.innerHTML = habitos.map(h => 
                    `<div>
                        <strong>${h.titulo}</strong> - ${h.tempo} min
                        <button onclick="excluirHabito(${h.id})">Excluir</button>
                    </div>`
                ).join('');
            } catch (error) {
                alert('Erro ao carregar hábitos: ' + error.message);
            }
        }
        
        async function excluirHabito(id) {
            if (!confirm('Deseja excluir este hábito?')) return;
            
            try {
                const response = await fetch(`${API_URL}/habits/${id}`, {
                    method: 'DELETE'
                });
                
                if (response.ok) {
                    alert('Hábito excluído!');
                    carregarHabitos();
                }
            } catch (error) {
                alert('Erro ao excluir: ' + error.message);
            }
        }
    </script>
</body>
</html>
```

---

## 📱 Principais Endpoints para o Front-End

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/login` | Autenticar usuário |
| POST | `/api/signup` | Cadastrar novo usuário |
| GET | `/api/habits` | Listar todos os hábitos |
| POST | `/api/habits` | Criar novo hábito |
| PUT | `/api/habits/<id>` | Atualizar hábito |
| DELETE | `/api/habits/<id>` | Excluir hábito |

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Erro: "Port 5000 already in use"
Mate o processo que está usando a porta:
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### CORS Error no Front-End
Certifique-se de que o servidor está rodando em `http://localhost:5000` e não em outro domínio.

---

## 📚 Documentação Completa

- **API Completa:** Veja `API_DOCS.md`
- **Arquitetura:** Veja `README.md`

---

## 🎨 Próximos Passos

1. **Configure o Front-End** para usar `http://localhost:5000/api`
2. **Implemente autenticação** no front usando o token JWT
3. **Teste todos os endpoints** antes de integrar
4. **Adicione validações** no front para melhorar UX

---

## ✅ Checklist de Integração

- [ ] Servidor rodando em `http://localhost:5000`
- [ ] Front-end conecta com sucesso na API
- [ ] Login funciona e retorna token
- [ ] Cadastro cria usuários corretamente
- [ ] CRUD de hábitos funciona completamente
- [ ] Erros são tratados adequadamente no front

---

**Pronto para integrar! 🚀**
