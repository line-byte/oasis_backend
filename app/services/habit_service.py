import os
import json
from datetime import datetime


HABITS_FILE = "data/habitos.json"


def carregar_habitos():
    """Carrega hábitos do arquivo JSON"""
    try:
        if os.path.exists(HABITS_FILE):
            with open(HABITS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        return []


def salvar_habitos(habitos):
    """Salva hábitos no arquivo JSON"""
    with open(HABITS_FILE, 'w', encoding='utf-8') as file:
        json.dump(habitos, file, ensure_ascii=False, indent=4)


def gerar_id_habito(habitos):
    """Gera um ID único para novo hábito"""
    if not habitos:
        return 1
    return max(h.get('id', 0) for h in habitos) + 1


def listar_habitos():
    """Retorna todos os hábitos"""
    return carregar_habitos()


def buscar_habito_por_id(habito_id):
    """Busca um hábito específico pelo ID"""
    habitos = carregar_habitos()
    for habito in habitos:
        if habito.get('id') == habito_id:
            return habito
    return None


def criar_habito(titulo, tempo, user_id=None):
    """Cria um novo hábito"""
    if not titulo or not tempo:
        return {"sucesso": False, "mensagem": "Título e tempo são obrigatórios"}
    
    habitos = carregar_habitos()
    
    novo_habito = {
        "id": gerar_id_habito(habitos),
        "titulo": titulo,
        "tempo": tempo,
        "data_criacao": str(datetime.now().date()),
        "user_id": user_id
    }
    
    habitos.append(novo_habito)
    salvar_habitos(habitos)
    
    return {"sucesso": True, "mensagem": "Hábito criado com sucesso", "habito": novo_habito}


def atualizar_habito(habito_id, titulo=None, tempo=None):
    """Atualiza um hábito existente"""
    habitos = carregar_habitos()
    
    for habito in habitos:
        if habito.get('id') == habito_id:
            if titulo is not None:
                habito['titulo'] = titulo
            if tempo is not None:
                habito['tempo'] = tempo
            
            salvar_habitos(habitos)
            return {"sucesso": True, "mensagem": "Hábito atualizado com sucesso", "habito": habito}
    
    return {"sucesso": False, "mensagem": "Hábito não encontrado"}


def excluir_habito(habito_id):
    """Exclui um hábito"""
    habitos = carregar_habitos()
    
    for i, habito in enumerate(habitos):
        if habito.get('id') == habito_id:
            habito_removido = habitos.pop(i)
            salvar_habitos(habitos)
            return {"sucesso": True, "mensagem": "Hábito excluído com sucesso", "habito": habito_removido}
    
    return {"sucesso": False, "mensagem": "Hábito não encontrado"}
