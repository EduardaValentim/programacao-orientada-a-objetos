turno = str(input('Digite o turno que vcê estuda: M, V ou N? ')).lower()

if turno == 'm':
	print('Bom dia!')
elif turno == 'v':
	print('Boa Tarde!')
elif turno == 'n':
	print('Boa Noite!')
else:
	print('Valor Inválido!')