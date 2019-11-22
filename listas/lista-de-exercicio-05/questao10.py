import random

print('{:-^30}'.format('Jogo de Craps'))

inicio = ''
jogada = 0
pontos = 0

print('Para sair digite 1')

while(inicio != '1'):
	jogada += 1
	inicio = input('Aperte qualquer tecla para o jogo continuar! ')
	if inicio == '1':
		print('Jogo encerrado')
	else:
		valor = random.randint(2, 12)
		print('Valor do dado: {}'.format(valor))
		if jogada == 1:
			if valor == 7 or valor == 11:
				print('Você conseguiu um natural, PARABÉNS!!!')
				print(' ')
				pass
			elif valor == 2 or valor == 3 or valor == 12:
				print('Craps! Não desanime tente outra vez.')
				print(' ')
				pass
			else:
				pontos = valor
				pass
		else:
			if valor == 7:
				print('Você não conseguiu seu ponto a tempo e isso te leva ao THE END!')
				print(' ')
				pass
			elif pontos == valor:
				print('Você conseguiu, PARABÉNS!!!')
				print(' ')
				pass
