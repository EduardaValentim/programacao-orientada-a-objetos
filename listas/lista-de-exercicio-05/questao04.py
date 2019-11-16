def sinal(numero):
	if numero > 0:
		num = 'P'
		return num
	else:
		num = 'N'
		return num

numero = float(input('Digite um número: '))
print(sinal(numero))