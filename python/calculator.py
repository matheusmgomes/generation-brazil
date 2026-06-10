def somar(a, b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a,b):
    if b == 0:
        return "Divisão por zero"
    return a/b

def potencia(a, b):
    return a**b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não existe raiz quadrada de número negativo"
    return a**0.5

continuar = 'S'

while continuar.upper() == 'S':
    print('----- CALCULADORA -----')

    opcao = input("\nSelecione a sua operação:\n1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n5-Potencia\n6-Raiz Quadrada\n")
    if opcao == '6':
        num1 = float(input("Digite o número: "))
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        

    if opcao == '1':
        print("Resultado = ", somar(num1, num2))
    elif opcao == '2':
        print("Resultado = ", subtrair(num1, num2))
    elif opcao == '3':
        print("Resultado = ", multiplicar(num1,num2))
    elif opcao == '4':
        print("Resultado = ", dividir(num1, num2))
    elif opcao == '5':
        print("Resultado = ", potencia(num1, num2))
    elif opcao == '6':
        print("Resultado = ", raiz_quadrada(num1))
    else:
        print("Opção inválida!")

    continuar = input("Deseja continuar? (S/N):")

print("Calculadora encerrada!")