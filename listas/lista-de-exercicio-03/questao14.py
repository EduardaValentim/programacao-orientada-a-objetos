nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media_aproveitamento = (nota1 + nota2) / 2

if 9 <= media_aproveitamento <= 10:
	print('Suas notas {} e {} resulta \nNa média de aproveitamento de {}'.format(nota1, nota2, media_aproveitamento))
	print('Enquadrando-se no conceito A')
	print('E por isso você está Aprovado!')
elif 7.5 <= media_aproveitamento < 9:
	print('Suas notas {} e {} resulta \nNa média de aproveitamento de {}'.format(nota1, nota2, media_aproveitamento))
	print('Enquadrando-se no conceito B')
	print('E por isso você está Aprovado!')
elif 6 <= media_aproveitamento < 7.5:
	print('Suas notas {} e {} resulta \nNa média de aproveitamento de {}'.format(nota1, nota2, media_aproveitamento))
	print('Enquadrando-se no conceito C')
	print('E por isso você está Aprovado!')
elif 4 <= media_aproveitamento < 6:
	print('Suas notas {} e {} resulta \nNa média de aproveitamento de {}'.format(nota1, nota2, media_aproveitamento))
	print('Enquadrando-se no conceito D')
	print('E por isso você está Reprovado!')
elif 0 <= media_aproveitamento < 4:
	print('Suas notas {} e {} resulta \nNa média de aproveitamento de {}'.format(nota1, nota2, media_aproveitamento))
	print('Enquadrando-se no conceito E')
	print('E por isso você está Reprovado!')
else:
	print('Valor Inválido')