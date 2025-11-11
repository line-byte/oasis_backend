import json 
from datetime import date
import os

bps ='./data/sensor.json'

def salvar(bpms):
    with open(bps, "w", encoding="utf-8") as s:
        return json.dump(bpms,s,indent=4,ensure_ascii=False)
    
def carregar():
    if os.path.exists(bps):
        with open(bps, "r", encoding="utf-8") as s:
            return json.load(s)
    return []


def criar_medida(bpms):
    tempo_medido = input("Tempo de prática (em minutos): ")

    bpm = {
        "id": len(bpms) + 1,
        "bpms": int(input("insira aqui os bpms medidos")), 
        "tempo": tempo_medido,
        "data_criacao": str(date.today())
    }

    bpms.append(bpm)
    salvar(bpms)
    print(f"nova medição criada com sucesso!\n")
    
def ler_todos(bpms):

    if not bpms:
        print("Nenhuma medição cadastrada ainda.\n")
        return

    print("\n📚 historico de bpms:")
    for s in bpms:
        print(f"ID: {s['id']} | {s['bpms']} - {s['tempo']} - {s['data_criacao']}")
    print()

def ler_um(bpms):
    if not bpms:
        print("Nenhuma medição cadastrada ainda.\n")
        return

    try:
        id_medida = int(input("Digite o ID da medição: "))
        for h in bpms:
            if h["id"] == id_medida:
                print("\n📚 Detalhes da medida:")
                print(f"Data de Criação: {h['data_criacao']}")
                print(f"bpms: {h['bpms']}")
                print(f"Tempo: {h['tempo']}")
                
                return
        print("medida não encontrada.\n")
    except ValueError: 
        print("ID inválido.\n")

def atualizar_medida(bpms):
    ler_todos(bpms)
    try:
        id_medida = int(input("Digite o ID da medida que deseja atualizar: "))
        for s in bpms:
            if s["id"] == id_medida:
                print(f"Editando: {s['bpms']}")
                s["bpms"] = input("insira nova medição: ") or s["bpms"]
                s["tempo"] = input("Novo tempo (em minutos): ") or s["tempo"]
                s["data_criacao"] = input("Nova data de criação (YYYY-MM-DD): ") or s["data_criacao"]
                salvar(bpms)
                print("aferição atualizada com sucesso!\n")
                return
        print("medida não encontrada.\n")
    except ValueError:
        print("ID inválido.\n")

def excluir_medida(bpms):
    ler_todos(bpms)
    try:
        id_medida = int(input("Digite o ID da medida que deseja excluir: "))
        for s in bpms:
            if s["id"] == id_medida:
                bpms.remove(s)
                salvar(bpms)
                print(f"medida '{s['bpms']}' removida com sucesso!\n")
                return
        print("medida não encontrada.\n")
    except ValueError:
        print("ID inválido.\n")