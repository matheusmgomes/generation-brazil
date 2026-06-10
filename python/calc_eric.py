#Exercicio: Desenvolver uma calculadora mais completa que permita ao usuário realizar diversas operações matemáticas através de um menu interativo.
#Calculadora cientifica

#Importar biblioteca math para funções matemáticas avançadas
import math
#Importar biblioteca os para limpar a tela do terminal
import os

#Função para exibir o menu de opções para o usuário
def menu():
    opcoes = [
        ("1 - Soma",           "6 - Raiz Quadrada"),
        ("2 - Subtração",      "7 - Média"),
        ("3 - Multiplicação",  "8 - Expressão"),
        ("4 - Divisão",        "9 - Histórico"),
        ("5 - Potência",       "0 - Sair"),
    ]

    print("==============================================")
    print("\033[1m" + "Calculadora Científica".center(46) + "\033[0m")
    print("==============================================")
    for esquerda, direita in opcoes:
        print(f"  {esquerda:<25}{direita}")
    print("==============================================")

def soma(*numeros):
    return sum(numeros)

def subtracao(*numeros):
    return numeros[0] - sum(numeros[1:])

def multiplicacao(*numeros):
    return math.prod(numeros)

def divisao(a, b):    
    if b <= 0:
        print("Não é possível dividir por zero ou por um número negativo.")
        return None
    else:
        return a / b

def potencia(a, b):
    if a < 0 and b < 0:
        print("Não é possível calcular a potência de uma base negativa com um expoente negativo.")
        return None
    else:
        return math.pow(a, b)

def raiz_quadrada(a):
    if a < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo.")
        return None
    else:
        return math.sqrt(a)

def media(*args):
    if len(args) == 0:
        print("Nenhum número fornecido para calcular a média.")
        return None
    else:
        return sum(args) / len(args)

def expressao_matematica(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except Exception as e:
        print(f"Erro ao avaliar a expressão: {e}")
        return None

def historico(historico_operacoes):
    if not historico_operacoes:
        print("Nenhuma operação realizada ainda.")
    else:
        print("==============================================")
        print("Histórico da Sessão:\n")
        for operacao in historico_operacoes:
            print(operacao)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Variável para armazenar a opção escolhida pelo usúario
opcao = ""

#Lista para armazenar o histórico das operações realizadas durante a sessão
historico_operacoes = []

#Loop principal para exibir o menu e processar as opções escolhidas pelo usúario
while opcao != "0":
    menu()
    opcao = input("Escolha uma opção: ")

    #Processar a opção escolhida pelo usuário e chamar a função correspondente, além de armazenar o resultado no histórico de operações
    if opcao == "1":
        qntd_numeros = int(input("Quantos números quer somar? "))
        numeros = []
        for i in range(qntd_numeros):
            numero = float(input(f"Digite o número {i+1}: "))
            numeros.append(numero)

        resultado = soma(*numeros)
        print(f"\nResultado: {resultado}")
        historico_operacoes.append(f"Soma: {' + '.join(str(n) for n in numeros)} = {resultado}")

    elif opcao == "2":
        qntd_numeros = int(input("Quantos números quer subtrair? "))
        numeros = []
        for i in range(qntd_numeros):
            numero = float(input(f"Digite o número {i+1}: "))
            numeros.append(numero)

        resultado = subtracao(*numeros)
        print(f"\nResultado: {resultado}")
        historico_operacoes.append(f"Subtração: {' - '.join(str(n) for n in numeros)} = {resultado}")

    elif opcao == "3":
        qntd_numeros = int(input("Quantos números quer multiplicar? "))
        numeros = []
        for i in range(qntd_numeros):
            numero = float(input(f"Digite o número {i+1}: "))
            numeros.append(numero)
        
        resultado = multiplicacao(*numeros)
        print(f"\nResultado: {resultado}")
        historico_operacoes.append(f"Multiplicação: {' * '.join(str(n) for n in numeros)} = {resultado}")

    elif opcao == "4":
        qntd_numeros = int(input("Quantos números quer dividir? "))
        if qntd_numeros < 2:
            print("É necessário fornecer pelo menos dois números para realizar a divisão.")
        else:
            numeros = []
            for i in range(qntd_numeros):
                numero = float(input(f"Digite o número {i+1}: "))
                numeros.append(numero)

            resultado = numeros[0]
            for num in numeros[1:]:
                resultado = divisao(resultado, num)
                if resultado is None:
                    break

            if resultado is not None:
                print(f"\nResultado: {resultado}")
                historico_operacoes.append(f"Divisão: {' / '.join(str(n) for n in numeros)} = {resultado}")
            
    elif opcao == "5":
        a = float(input("Digite a base: "))
        b = float(input("Digite o expoente: "))
        resultado = potencia(a, b)
        if resultado is not None:
            print(f"\nResultado: {resultado:.2f}")
            historico_operacoes.append(f"Potência: {a} ^ {b} = {resultado}")

    elif opcao == "6":
        a = float(input("Digite um número para calcular a raiz quadrada: "))
        resultado = raiz_quadrada(a)
        if resultado is not None:
            print(f"\nResultado: {resultado:.2f}")
            historico_operacoes.append(f"Raiz Quadrada: √{a} = {resultado}")

    elif opcao == "7":
        numeros_str = input("Digite os números separados por vírgula para calcular a média: ")
        numeros = [float(num) for num in numeros_str.split(",")]
        resultado = media(*numeros)
        if resultado is not None:
            print(f"\nMédia: {resultado:.2f}")
            historico_operacoes.append(f"Média: {numeros} = {resultado}")

    elif opcao == "8":
        expressao = input("Digite a expressão matemática para avaliar: ")
        resultado = expressao_matematica(expressao)
        if resultado is not None:
            print(f"\nResultado: {resultado}")
            historico_operacoes.append(f"Expressão Matemática: {expressao} = {resultado}")
    
    elif opcao == "9":
        historico(historico_operacoes)

    elif opcao == "0":
        print("==============================================") 
        print(f"Total de cálculos realizados: {len(historico_operacoes)}")
        print("==============================================")        
        if historico_operacoes:
            resultados = [float(operacao.split('=')[-1].strip()) for operacao in historico_operacoes if '=' in operacao]
            maior_resultado = max(resultados)
            print(f"Maior resultado obtido: {maior_resultado}")
        else:
            print("Nenhum cálculo realizado para determinar o maior resultado.")
        print("==============================================")
        print("Encerrando a calculadora. Até mais!")
        
    else:
        print("==============================================")
        print("Opção inválida. Por favor, escolha uma opção válida.")

    input("Pressione Enter para continuar...")
    limpar_tela()