from funcoes import carregar_dados
from sensores_crud import criar_medida, ler_todos, ler_um, atualizar_medida, excluir_medida
from relatorio_sensores import exibir_menu_relatorios

def exibir_menu():
    bpms = carregar_dados()

    while True:
        print("========== 🎞️ MENU – GERENCIADOR DE BATIMENTOS ==========")
        print("1. criar uma medição nova")
        print("2. ver historico de bpms")
        print("3. ver um bpm em especifico")
        print("4. aferir bpms")
        print("5. Excluir aferições do historico")
        print("6. Relatórios")
        print("7. Sair")
        print("======================================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_medida(bpms)
        elif opcao == "2":
            ler_todos(bpms)
        elif opcao == "3":
            ler_um(bpms)
        elif opcao == "4":
            atualizar_medida(bpms)
        elif opcao == "5":
            excluir_medida(bpms)
        elif opcao == "6":
            exibir_menu_relatorios()
        elif opcao == "7":
            print("👋 Saindo... até a próxima!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")