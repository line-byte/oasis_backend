import json 
from datetime import datetime
import os

BPS = "./data/sint.json"

def salvar(bpms):
    with open(BPS, "w", encoding="utf-8") as dados:
        return json.dump(bpms,dados,indent=4,ensure_ascii=False)
    
def carregar():
    if os.path.exists(BPS):
        with open(BPS, "r", encoding="utf-8") as dados:
            return json.load(dados)
    return []

'''provavelmente usarei um serialRead para entrar os dados ou algo assim aqui'''

bpms =[]
sessao = "on"
agora = datetime.now()


bpm_inicial = [input(" insira o bpm inicial aqui "), agora.strftime("%d/%m %H:%M") ]
    
while sessao == "on":
    bpms=carregar()
    bpm = {f"bpm inicial": bpm_inicial, "bpms": (input(" insira aqui os bpms ")), "horario": agora.strftime("%d/%m %H:%M"),}
    bpms.append(bpm)
    if len(bpms) > 5:
        bpms.pop(0)    
    salvar(bpms)
    
    
    parar = input(" finalizar sessao? ")
    if parar == "sim" or parar == "s" or parar == "S":
        break
    else: sessao = "on"

'''a saída vai passar por ajustes a fim de ficar mais bonito'''

print (bpms[-1])
