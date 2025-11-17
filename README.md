# OASIS - Backend (API)

## Visão geral

Este repositório contém a API do OASIS (ambiente de desenvolvimento). A documentação original foi movida para `docs_backup/` e este README sintetiza as informações principais para integração e uso rápido.

## Principais conceitos

- Autenticação: JWT (login/signup).
- Recursos principais: `habits` (hábitos), `categories` (categorias), `journal` (registros diários), `users`.
- Persistência (desenvolvimento): arquivos JSON em `data/`.

## Índice

- [Endpoints](#endpoints)
- [Como integrar](#como-integrar)
- [Fluxos comuns](#fluxos-comuns)
- [Operações (CRUD)](#opera%C3%A7%C3%B5es-crud)
- [Dados e backup](#dados-e-backup)
- [Executar localmente](#executar-localmente)
- [Referências](#refer%C3%AAncias)

## Endpoints

Base: `/api`

### Auth

- `POST /api/login`

  Payload:

  ```json
  { "email": "user@example.com", "senha": "password" }
  ```

  Retorna: `{ token, usuario: { id, nome, email } }`

- `POST /api/signup`

  Payload:

  ```json
  { "nome": "Fulano", "email": "f@ex.com", "senha": "senha" }
  ```

### Users

- `GET /api/users`

### Habits

- `GET /api/habits`
- `GET /api/habits/user/<user_id>`
- `POST /api/habits`

  Exemplo de payload:

  ```json
  {
    "titulo": "Meditar",
    "descricao": "10 min",
    "categoria": 1,
    "repetir": true,
    "tipo_repeticao": "diario",
    "user_id": 1
  }
  ```

- `PUT /api/habits/<id>`
- `DELETE /api/habits/<id>`
- `POST /api/habits/<id>/toggle` (alternar completado)

### Categories

- `GET /api/categories`
- `GET /api/categories?user_id=<id>`
- `POST /api/categories`
- `PUT /api/categories/<id>`
- `DELETE /api/categories/<id>`

### Journal

- `GET /api/journal`
- `GET /api/journal/user/<user_id>`
- `GET /api/journal/user/<user_id>/date/<YYYY-MM-DD>`

  > Observação: este endpoint retorna uma lista de registros para a data — o sistema permite múltiplas entradas por dia.

- `POST /api/journal`

  Exemplo de payload:

  ```json
  { "conteudo": "Hoje fiz X", "user_id": 1, "data": "2025-11-17" }
  ```

- `PUT /api/journal/<id>`
- `DELETE /api/journal/<id>`

## Como integrar

- Autentique via `POST /api/login` para obter o token JWT.
- Inclua o token no header `Authorization: Bearer <token>` nas chamadas que requerem autenticação.
- O frontend padrão deste projeto usa `localStorage` para armazenar `oasis_token` e `oasis_user`.

## Fluxos comuns

1. Signup → Login → Criar categoria → Criar hábito → Marcar hábito concluído → Registrar diário
2. Repetição mensal: o backend utiliza `dateutil.relativedelta` para calcular corretamente a próxima ocorrência em meses com dias diferentes (ex.: fevereiro).

## Operações (CRUD)

- Criação: `POST` com JSON no corpo. Retorna `201 Created` quando criado.
- Atualização: `PUT` com JSON. Retorna `200 OK` quando atualizado.
- Remoção: `DELETE`. Retorna `200 OK` quando excluído.

## Dados e backup

- Os dados de desenvolvimento ficam em `data/` (ex.: `users.json`, `habitos.json`, `categorias.json`, `registros_diarios.json`).
- Faça backup desses arquivos antes de edições manuais.

## Executar localmente

1. Ative o virtualenv:

```bash
source OasisVenv/bin/activate
```

2. (Opcional) Instale dependências:

```bash
pip install -r requirements.txt
```

3. Rode a API em desenvolvimento:

```bash
python app.py
```

O servidor por padrão roda em `http://127.0.0.1:5000`.

## Referências

- Documentação detalhada e arquivos históricos foram movidos para `docs_backup/` neste repositório.

---

_Este README foi gerado para consolidar a documentação do backend. Arquivos originais foram preservados em `docs_backup/`._
