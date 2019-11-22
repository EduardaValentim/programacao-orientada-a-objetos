def reverso(num):
	resultado = num[::-1]
	return resultado

numero = str(input('Digite um número inteiro: ')).strip()
print('O reverso desse número é {}'.format(reverso(numero)))
