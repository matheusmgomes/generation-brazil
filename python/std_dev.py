def media(lista):
  soma = 0
  for x in lista:
    soma += x
  
  return soma / len(lista)

def mediana(lista):
  lista_ordenada = sorted(lista)
  meio = len(lista_ordenada) // 2

  if len(lista_ordenada) % 2 != 0:
    return lista_ordenada[meio]
  else:
    num1 = lista_ordenada[meio - 1]
    num2 = lista_ordenada[meio]

    return (num1 + num2) / 2

def moda(lista):
  freq = {}
  for num in lista:
    if num in freq:
      freq[num] += 1
    else:
      freq[num] = 1
  
  return max(freq, key=freq.get)

def pontuacao_desvio(lista, media):
  pont_lista = []

  for x in lista:
    pont_lista.append(x - media)

  return pont_lista

def desvio_quadratico(lista):
  return [x**2 for x in lista]

def soma_desvio_quadratico(lista):
  soma = 0
  for x in lista:
    soma += x

  return soma

def variancia(soma, lista):
  return soma / len(lista)

def desvio_padrao(lista):
  avg = media(lista)
  print(f"Média: {avg}")

  pont_dev = pontuacao_desvio(lista, avg)
  print(f"Pontuação de desvio: {pont_dev}")

  quad_dev = desvio_quadratico(pont_dev)
  print(f"Desvio quadrático: {quad_dev}")

  soma_dev_quad = soma_desvio_quadratico(quad_dev)
  print(f"Soma do desvio quadrático: {soma_dev_quad}")

  var = variancia(soma_dev_quad, quad_dev)
  print(f"Variância: {var}")

  return var ** 0.5



lista = [50, 50, 55, 60, 70, 80, 90]

print("Mediana: ", mediana(lista))
print("Moda: ", moda(lista))
print("Desvio padrão: ", desvio_padrao(lista))