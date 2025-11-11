from sensores_crud import carregar

def relatorio_quantidade():
    habitos = carregar()
    print(f"\nTotal de hábitos cadastrados: {len(habitos)}\n")


def relatorio_por_medida():
    habitos = carregar()
    if not habitos:
        print("Nenhum hábito cadastrado.\n")
        return

    medidas = {}
    for s in habitos:
        title = s["bpms"].title()
        medidas[title] = medidas.get(title, 0) + 1

    print("\nmedidas por bpm:")
    for bpm, qtd in medidas.items():
        print(f"- {bpm}: {qtd}")
    print()


def relatorio_por_data():
    historico = carregar()
    if not historico:
        print("Nenhum historico cadastrado.\n")
        return

    datas = {}
    for s in historico:
        data = s["data_criacao"].title()
        datas[data] = datas.get(data, 0) + 1

    print("\nMedidas por Data:")
    for data, qtd in datas.items():
        print(f"- {data}: {qtd}")
    print()


def exibir_menu_relatorios():
    """Menu de relatórios para o console."""
    while True:
        print("========== RELATÓRIOS ==========")
        print("1. Total de medições cadastradas")
        print("2. Quantidade por medição")
        print("3. Quantidade por data de criação")
        print("4. Voltar ao menu principal")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_quantidade()
        elif opcao == "2":
            relatorio_por_medida()
        elif opcao == "3":
            relatorio_por_data()
        elif opcao == "4":
            print("↩Voltando ao menu principal...\n")
            break
        else:
            print("Opção inválida!\n")