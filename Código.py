import random

aleatorio = list(range(1,31))
random.shuffle(aleatorio)
print(f'Os números aleatorios são: \n{aleatorio}')
print()

#1º forma de alinhar os números de forma crescente
listaOrdenada = sorted(aleatorio)
print(listaOrdenada)

#2º forma de ordenar os números de forma crescente
aleatorio.sort()
print(aleatorio)

#3º forma de organizar os números de forma crescente
listaOrdenada = []

for i in range(len(aleatorio)):
	menorNumero = min(aleatorio)
	listaOrdenada.append(menorNumero)
	aleatorio.remove(menorNumero)

print(f'Os números ordenados são: \n{listaOrdenada}')