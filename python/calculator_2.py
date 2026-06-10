import math

def menu():
    print("-*-CALCULADORA AVANÇADA-*-")
    print("1 - Somar vários números")
    print("2 - Subtrair dois números")
    print("3 - Multiplicar vários números")
    print("4 - Dividir dois números")
    print("5 - Potencia")
    print("6 - Raiz Quadrada")
    print("7 - Resolver expressão numérica")
    print("8 - Sair")

def somar_varios():
    quantidade = int(input("Quantos números deseja somar?"))
    soma = 0

    for i in range(quantidade):
        numero = float(input(f"Digite o {i+1}º número: "))
        soma += numero

    return soma

def mult_varios():
    quantidade = int(input("Quantos números deseja multiplicar?"))
    mult = 1

    for i in range(quantidade):
        numero = float(input(f"Digite o {i+1}º número: "))
        mult *= numero

    return mult

def subtrair(a,b):
    return a-b

def dividir(a,b):
    if b == 0:
        return "Divisão por zero"
    return a/b

def potencia(a, b):
    return math.pow(a, b)

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não existe raiz quadrada de número negativo"
    return math.sqrt(a)

def resolver_expressao():
    expressao = input("Digite a expressão numérica: ")
    return eval(expressao)

opcao = ""

while opcao != "8":
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Resultado:", somar_varios())
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", subtrair(num1, num2))
    elif opcao == "3":
        print("Resultado:", mult_varios())
    elif opcao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", dividir(num1, num2))
    elif opcao == "5":
        base = float(input("Digite a base: "))
        exp = float(input("Digite o expoente: "))
        print("Resultado: ", potencia(base, exp))
    elif opcao == "6":
        num1 = float(input("Digite o primeiro número: "))
        print("Resultado: ", raiz_quadrada(num1))        
    elif opcao == "7":
        print("Resultado: ", resolver_expressao())
    elif opcao == '8':
        print("Calculadora encerrada!")
    else:
        print("Digite uma opção válida.")