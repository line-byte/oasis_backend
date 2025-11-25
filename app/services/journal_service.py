import os
import json
from datetime import datetime


JOURNAL_FILE = "data/registros_diarios.json"


def carregar_registros():
    try:
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []


def salvar_registros(registros):
    with open(JOURNAL_FILE, 'w', encoding='utf-8') as file:
        json.dump(registros, file, ensure_ascii=False, indent=4)


def gerar_id_registro(registros):
    if not registros:
        return 1
    return max(r.get('id', 0) for r in registros) + 1


def listar_registros():
    return carregar_registros()


def listar_registros_por_usuario(user_id):
    registros = carregar_registros()
    registros_usuario = [r for r in registros if r.get('user_id') == user_id]
    registros_usuario.sort(key=lambda x: x.get('data_criacao', ''), reverse=True)
    return registros_usuario


def buscar_registro_por_id(registro_id):
    registros = carregar_registros()
    for registro in registros:
        if registro.get('id') == registro_id:
            return registro
    return None


def buscar_registro_por_data(user_id, data):
    registros = carregar_registros()
    encontrados = [r for r in registros if r.get('user_id') == user_id and r.get('data') == data]
    return encontrados


def criar_registro(conteudo, user_id, data=None):
    if not conteudo or not user_id:
        return {"sucesso": False, "mensagem": "Conteúdo e ID do usuário são obrigatórios"}
    
    if not data:
        data = str(datetime.now().date())
    
    registros = carregar_registros()

    novo_registro = {
        "id": gerar_id_registro(registros),
        "conteudo": conteudo,
        "data": data,
        "user_id": user_id,
        "data_criacao": str(datetime.now().isoformat())
    }
    
    registros.append(novo_registro)
    salvar_registros(registros)
    
    return {"sucesso": True, "mensagem": "Registro criado com sucesso", "registro": novo_registro, "atualizado": False}


def atualizar_registro(registro_id, conteudo=None, user_id=None):
    registros = carregar_registros()
    
    for registro in registros:
        if registro.get('id') == registro_id:
            if user_id and registro.get('user_id') != user_id:
                return {"sucesso": False, "mensagem": "Você não tem permissão para editar este registro"}
            
            if conteudo is not None:
                registro['conteudo'] = conteudo
                registro['data_atualizacao'] = str(datetime.now().isoformat())
            
            salvar_registros(registros)
            return {"sucesso": True, "mensagem": "Registro atualizado com sucesso", "registro": registro}
    
    return {"sucesso": False, "mensagem": "Registro não encontrado"}


def excluir_registro(registro_id, user_id=None):
    registros = carregar_registros()
    
    for i, registro in enumerate(registros):
        if registro.get('id') == registro_id:
            if user_id and registro.get('user_id') != user_id:
                return {"sucesso": False, "mensagem": "Você não tem permissão para excluir este registro"}
            
            registro_removido = registros.pop(i)
            salvar_registros(registros)
            return {"sucesso": True, "mensagem": "Registro excluído com sucesso", "registro": registro_removido}
    
    return {"sucesso": False, "mensagem": "Registro não encontrado"}
