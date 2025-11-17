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

  # Oasis Backend - API REST

  Sistema de gerenciamento de hábitos saudáveis com autenticação de usuários.

  > Observação: o conteúdo histórico detalhado foi preservado a partir de `docs_backup/`. Esta versão incorpora as informações originais e adiciona notas sobre as funcionalidades e correções implementadas recentemente.

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

  Base: `/api`

  ### Autenticação

  - `POST /api/login` — Login de usuário

    Payload:

    ```json
    { "email": "user@example.com", "senha": "password" }
    ```

    Retorna: `{ token, usuario: { id, nome, email } }`

  - `POST /api/signup` — Cadastro de novo usuário

    Payload:

    ```json
    { "nome": "Fulano", "email": "f@ex.com", "senha": "senha" }
    ```

  ### Users

  - `GET /api/users` — Listar usuários

  ### Habits (hábitos)

  - `GET /api/habits` — Listar todos os hábitos
  - `GET /api/habits/<id>` — Buscar hábito específico
  - `GET /api/habits/user/<user_id>` — Hábitos de um usuário
  - `POST /api/habits` — Criar novo hábito

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

  - `PUT /api/habits/<id>` — Atualizar hábito
  - `DELETE /api/habits/<id>` — Excluir hábito
  - `POST /api/habits/<id>/toggle` — Alterna campo `completado`

  ### Categories (categorias)

  - `GET /api/categories`
  - `GET /api/categories?user_id=<id>`
  - `POST /api/categories`
  - `PUT /api/categories/<id>`
  - `DELETE /api/categories/<id>`

  ### Journal (registros diários)

  - `GET /api/journal` — Listar registros
  - `GET /api/journal/user/<user_id>` — Registros de um usuário
  - `GET /api/journal/user/<user_id>/date/<YYYY-MM-DD>` — Registros em uma data

    > Observação: este endpoint retorna uma lista de registros para a data — o sistema permite múltiplas entradas por dia.

  - `POST /api/journal` — Criar registro

    Exemplo de payload:

    ```json
    { "conteudo": "Hoje fiz X", "user_id": 1, "data": "2025-11-17" }
    ```

  - `PUT /api/journal/<id>` — Atualizar registro
  - `DELETE /api/journal/<id>` — Remover registro

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

     ```text
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

  ## Como integrar

  - Autentique via `POST /api/login` para obter o token JWT.
  - Inclua o token no header `Authorization: Bearer <token>` nas chamadas que requerem autenticação.
  - O frontend padrão deste projeto usa `localStorage` para armazenar `oasis_token` e `oasis_user`.

  ## Fluxos comuns

  1. Signup → Login → Criar categoria → Criar hábito → Marcar hábito concluído → Registrar diário

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

  ## Alterações recentes / Notas de migração

  - Modelo de repetição de hábitos: a antiga representação numérica de frequência foi substituída por campos `repetir: bool` e `tipo_repeticao: "diario" | "semanal" | "mensal"`. A lógica de cálculo da próxima ocorrência utiliza `dateutil.relativedelta` para lidar corretamente com meses de tamanhos diferentes (ex.: fevereiro).

  - Registros diários: o backend passou a permitir múltiplos registros por dia. O endpoint `GET /api/journal/user/<user_id>/date/<YYYY-MM-DD>` retorna agora uma lista de entradas para a data.

  - Date handling front-end: o frontend agora envia datas no formato `YYYY-MM-DD` com base na data local (evitando off-by-one causado por `toISOString()` e interpretação UTC).

  - Observação sobre dados existentes: se você tiver registros antigos com datas afetadas por conversões UTC, é recomendável revisar `data/registros_diarios.json` e normalizar as datas (posso fornecer um script seguro para isso, com backup automático).

  ## Referências

  - Documentação detalhada e arquivos históricos foram movidos para `docs_backup/` neste repositório.

  ---

  _README consolidado: preserva a documentação histórica e acrescenta notas sobre correções/funcionalidades recentes. Arquivos originais permanecem em `docs_backup/`._
