import os
from getpass import getpass

# Dicionário responsável por armazenar os serviços e suas senhas
senhas = {}


# Função responsável por limpar o terminal
def limpar_tela():

    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


# Função responsável por exibir o menu principal
def mostrar_menu():

    print("""
╔══════════════════════════════════════════════╗
║             GERENCIADOR DE SENHAS            ║
╠══════════════════════════════════════════════╣
║                                              ║
║  1 - Adicionar senha                         ║
║  2 - Listar serviços                         ║
║  3 - Buscar senha                            ║
║  4 - Remover senha                           ║
║                                              ║
║  0 - Sair                                    ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


# Função para adicionar uma nova senha
def adicionar_senha():

    print("\n===== ADICIONAR SENHA =====\n")

    site = input("Digite o nome do serviço: ")

    # A senha não aparece enquanto é digitada
    senha = getpass("Digite a senha: ")

    limpar_tela()

    # Adiciona o serviço e a senha ao dicionário
    senhas[site] = senha

    print("✓ Senha cadastrada com sucesso!")


# Função para listar os serviços cadastrados
def listar_senhas():

    print("\n===== SERVIÇOS CADASTRADOS =====\n")

    if len(senhas) == 0:

        print("Nenhum serviço cadastrado.")

    else:

        contador = 1

        # Exibe somente os nomes dos serviços
        for site in senhas:

            print(f"{contador}. {site}")

            contador += 1


# Função para buscar uma senha específica
def buscar_senha():

    print("\n===== BUSCAR SENHA =====\n")

    site = input("Digite o serviço: ")

    limpar_tela()

    if site in senhas:

        print("===== SENHA ENCONTRADA =====\n")

        print("Serviço:", site)

        print("Senha:", senhas[site])

    else:

        print("Serviço não encontrado.")


# Função para remover uma senha
def remover_senha():

    print("\n===== REMOVER SENHA =====\n")

    site = input("Digite o serviço que deseja remover: ")

    limpar_tela()

    if site in senhas:

        del senhas[site]

        print("✓ Serviço removido com sucesso!")

    else:

        print("Serviço não encontrado.")


opcao = ""

# Loop principal do programa
while opcao != "0":

    limpar_tela()

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    limpar_tela()

    if opcao == "1":

        adicionar_senha()

    elif opcao == "2":

        listar_senhas()

    elif opcao == "3":

        buscar_senha()

    elif opcao == "4":

        remover_senha()

    elif opcao == "0":

        print("""
╔══════════════════════════════════════════════╗
║                                              ║
║          PROGRAMA ENCERRADO COM SUCESSO      ║
║                                              ║
╚══════════════════════════════════════════════╝
""")

    else:

        print("Opção inválida.")

    # Mantém a mensagem na tela até o usuário pressionar ENTER
    if opcao != "0":

        input("\nPressione ENTER para voltar ao menu...")