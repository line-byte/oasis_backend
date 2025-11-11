import json
import os

ARQUIVO = "../data/habitos.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as h:
            return json.load(h)
    return []

def salvar_dados(habitos):
    with open(ARQUIVO, "w", encoding="utf-8") as h:
        json.dump(habitos, h, indent=4, ensure_ascii=False)
