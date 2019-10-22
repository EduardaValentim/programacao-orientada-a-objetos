numero = float(input('Qual valor? '))

if numero > 0:
	print('O número {:.1f} é POSITIVO!'.format(numero))
else:
	print('O número {:.1F} é NEGATIVO!'.format(numero))