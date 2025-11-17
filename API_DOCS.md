# API Documentation - Oasis Backend

Base URL: `http://localhost:5000`

## 🔐 Autenticação

### 1. Login
**Endpoint:** `POST /api/login`

**Request Body:**
```json
{
  "email": "usuario@example.com",
  "senha": "senha123"
}
```

**Response Success (200):**
```json
{
  "mensagem": "Login realizado com sucesso",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "usuario": {
    "id": 1,
    "nome": "João Silva",
    "email": "usuario@example.com"
  }
}
```

**Response Error (401):**
```json
{
  "erro": "Credenciais inválidas"
}
```

---

### 2. Cadastro
**Endpoint:** `POST /api/signup`

**Request Body:**
```json
{
  "nome": "João Silva",
  "email": "usuario@example.com",
  "senha": "senha123",
  "data_nasc": "1990-01-15",
  "idade": 33,
  "sexo": "M"
}
```

**Campos obrigatórios:** `email`, `senha`

**Response Success (201):**
```json
{
  "mensagem": "Usuário cadastrado com sucesso"
}
```

**Response Error (400):**
```json
{
  "erro": "Email já cadastrado"
}
```

---

### 3. Listar Usuários
**Endpoint:** `GET /api/users`

**Response Success (200):**
```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "email": "usuario@example.com",
    "idade": 33,
    "data_nascimento": "1990-01-15",
    "sexo": "M",
    "data_criacao": "2025-11-15"
  }
]
```

---

## 📋 Hábitos

### 1. Listar Todos os Hábitos
**Endpoint:** `GET /api/habits`

**Response Success (200):**
```json
[
  {
    "id": 1,
    "titulo": "Meditação",
    "tempo": "15",
    "data_criacao": "2025-11-15",
    "user_id": 1
  },
  {
    "id": 2,
    "titulo": "Exercício",
    "tempo": "30",
    "data_criacao": "2025-11-15",
    "user_id": 1
  }
]
```

---

### 2. Buscar Hábito por ID
**Endpoint:** `GET /api/habits/<id>`

**Exemplo:** `GET /api/habits/1`

**Response Success (200):**
```json
{
  "id": 1,
  "titulo": "Meditação",
  "tempo": "15",
  "data_criacao": "2025-11-15",
  "user_id": 1
}
```

**Response Error (404):**
```json
{
  "erro": "Hábito não encontrado"
}
```

---

### 3. Criar Novo Hábito
**Endpoint:** `POST /api/habits`

**Request Body:**
```json
{
  "titulo": "Leitura",
  "tempo": "20",
  "user_id": 1
}
```

**Campos obrigatórios:** `titulo`, `tempo`

**Response Success (201):**
```json
{
  "mensagem": "Hábito criado com sucesso",
  "habito": {
    "id": 3,
    "titulo": "Leitura",
    "tempo": "20",
    "data_criacao": "2025-11-17",
    "user_id": 1
  }
}
```

**Response Error (400):**
```json
{
  "erro": "Título e tempo são obrigatórios"
}
```

---

### 4. Atualizar Hábito
**Endpoint:** `PUT /api/habits/<id>`

**Exemplo:** `PUT /api/habits/3`

**Request Body:**
```json
{
  "titulo": "Leitura noturna",
  "tempo": "30"
}
```

**Response Success (200):**
```json
{
  "mensagem": "Hábito atualizado com sucesso",
  "habito": {
    "id": 3,
    "titulo": "Leitura noturna",
    "tempo": "30",
    "data_criacao": "2025-11-17",
    "user_id": 1
  }
}
```

**Response Error (404):**
```json
{
  "erro": "Hábito não encontrado"
}
```

---

### 5. Excluir Hábito
**Endpoint:** `DELETE /api/habits/<id>`

**Exemplo:** `DELETE /api/habits/3`

**Response Success (200):**
```json
{
  "mensagem": "Hábito excluído com sucesso",
  "habito": {
    "id": 3,
    "titulo": "Leitura noturna",
    "tempo": "30",
    "data_criacao": "2025-11-17",
    "user_id": 1
  }
}
```

**Response Error (404):**
```json
{
  "erro": "Hábito não encontrado"
}
```

---

## 🔧 Headers CORS

Todos os endpoints suportam requisições de qualquer origem (CORS configurado).

**Headers permitidos:**
- `Content-Type`
- `Authorization`

**Métodos permitidos:**
- `GET`, `POST`, `PUT`, `DELETE`, `OPTIONS`

---

## 📝 Exemplos de Uso com Fetch (JavaScript)

### Login
```javascript
const login = async (email, senha) => {
  const response = await fetch('http://localhost:5000/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email, senha })
  });
  
  const data = await response.json();
  
  if (response.ok) {
    localStorage.setItem('token', data.token);
    return data;
  } else {
    throw new Error(data.erro);
  }
};
```

### Criar Hábito
```javascript
const criarHabito = async (titulo, tempo, userId) => {
  const response = await fetch('http://localhost:5000/api/habits', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ titulo, tempo, user_id: userId })
  });
  
  const data = await response.json();
  
  if (response.ok) {
    return data.habito;
  } else {
    throw new Error(data.erro);
  }
};
```

### Listar Hábitos
```javascript
const listarHabitos = async () => {
  const response = await fetch('http://localhost:5000/api/habits');
  const habitos = await response.json();
  return habitos;
};
```

### Atualizar Hábito
```javascript
const atualizarHabito = async (id, titulo, tempo) => {
  const response = await fetch(`http://localhost:5000/api/habits/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ titulo, tempo })
  });
  
  const data = await response.json();
  
  if (response.ok) {
    return data.habito;
  } else {
    throw new Error(data.erro);
  }
};
```

### Excluir Hábito
```javascript
const excluirHabito = async (id) => {
  const response = await fetch(`http://localhost:5000/api/habits/${id}`, {
    method: 'DELETE'
  });
  
  const data = await response.json();
  
  if (response.ok) {
    return data;
  } else {
    throw new Error(data.erro);
  }
};
```

---

## 🚀 Como Testar

1. **Inicie o servidor:**
   ```bash
   python app.py
   ```

2. **Teste com curl:**
   ```bash
   # Login
   curl -X POST http://localhost:5000/api/login \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","senha":"123456"}'
   
   # Listar hábitos
   curl http://localhost:5000/api/habits
   ```

3. **Ou use ferramentas como:**
   - Postman
   - Insomnia
   - Thunder Client (VS Code Extension)
