def soma(n1, n2, n3):
	resultado = int(n1 + n2 + n3)
	return resultado

a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite mais um número: '))

print('A soma dos número é {}!'.format(soma(a, b, c)))
