import math

def soma(a, b):
    # soma = 0
    # user_input = input("Digite um número a ser somado ou uma letra para parar a soma: ")
    # while user_input.isdigit():
    #     soma += float(user_input)
    #     print("Resultado: ", soma)
    #     user_input = input("Digite um número a ser somado ou uma letra para parar a soma: ")
    
    # return soma
    return a+b

def subtrair(a, b):
    # num1 = float(input("Digite o primeiro número: "))
    # num2 = float(input("Digite o segundo número: "))

    # return num1 - num2
    return a - b

def multiplicacao(a, b):
    # mult = 1
    # user_input = input("Digite um número a ser somado ou uma letra para parar a multiplicação: ")
    # while user_input.isdigit():
    #     mult *= float(user_input)
    #     print("Resultado: ", mult)
    #     user_input = input("Digite um número a ser somado ou uma letra para parar a multiplicação: ")
    
    # return mult
    return a * b

def divisao(a, b):
    # num1 = float(input("Digite o primeiro número: "))
    # num2 = float(input("Digite o segundo número (diferente de zero): "))
    # if num2 == 0:
    #     return "Erro: Divisão por zero"
    # return num1 / num2
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def potencia(base, exp):
    # base = float(input("Digite a base: "))
    # exp = float(input("Digite o expoente: "))
    return math.pow(base, exp)

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não existe raiz quadrada de número negativo"
    return math.sqrt(a)


def media():
    div_media = int(input("Digite a quantidade de valores: "))

    if div_media <= 0:
        return "Não é possível realizar média para valores nulos ou negativos"
    
    soma = 0
    for i in range(div_media):
        num = float(input(f"Digite o {i+1}° número: "))
        soma += num

    return soma/div_media

def expressao():
    expressao = input("Digite a expressão numérica: ")
    return eval(expressao)

def menu():
    print("-*-CALCULADORA AVANÇADA-*-")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potencia")
    print("6 - Raiz Quadrada")
    print("7 - Média de vários números")
    print("8 - Expressão numérica")
    print("9 - Histórico")
    print("0 ou qualquer outra opção - Sair")


operations = []
maior_resultado = 0

option = '1'

while option.isdigit() and option != '0':
    menu()
    option = input("Digite a sua opção: ")
    result = 0

    if option == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = soma(num1, num2)
        print("Resultado: ", result)
        operations.append(f"{num1} + {num2} = {result}")
    elif option == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = subtrair(num1, num2)
        print("Resultado: ", result)
        operations.append(f"{num1} - {num2} = {result}")
    elif option == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = multiplicacao(num1, num2)
        print("Resultado: ", result)
        operations.append(f"{num1} * {num2} = {result}")
    elif option == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = divisao(num1, num2)
        print("Resultado: ", result)
        if result != "Erro: Divisão por zero":
            operations.append(f"{num1} * {num2} = {result}")
    elif option == '5':
        base = float(input("Digite a base: "))
        exp = float(input("Digite o expoente: "))
        result = potencia(base, exp)
        print("Resultado: ", result)
        operations.append(f"{num1} ^ {num2} = {result}")
    elif option == '6':
        num = float(input("Digite o número: "))
        result = raiz_quadrada(num)
        print("Resultado: ", result)
        operations.append(f"√{num} = {result}")
    elif option == '7':
        result = media()
        print("Resultado: ", result)
        operations.append(f"Média: {result}")
    elif option == '8':
        result = expressao()
        print("Resultado: ", result)
        operations.append(f"Expressão: {result}")
    elif option == '9':
        print("Histórico: ")
        for i in range(len(operations)):
            print(operations[i])
    else:
        print(f"Você realizou {len(operations)} operação(ões)")
        print(f"Maior resultado: {maior_resultado}")
        print("Finalizando calculadora!")
    
    if result > maior_resultado:
        maior_resultado = result
