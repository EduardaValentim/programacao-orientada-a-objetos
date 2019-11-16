n = int(input('digite um número: '))
lista = []
while n not in lista:
	for numero in range(1, n + 1):
		lista.append(numero)
		print(str(lista).strip('[]'))