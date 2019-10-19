altura = float(input('Digite sua altura em metros: '))
genero = input('Masculino ou Feminino: ').lower()
if genero == 'masculino':
	peso_ideal = (72.7 * altura) - 58
	print('O seu peso ideal seria de {:.2f}Kg!'.format(peso_ideal))
elif genero == 'feminino':
	peso_ideal = (62.1 * altura) - 44.7
	print('O seu peso ideal seria de {:.2f}Kg!'.format(peso_ideal))
else:
	print('Dados Inválidos!')