import random

print('{:-^30}'.format('Jogo de Craps'))

inicio = ''
jogada = 0
pontos = 0

print('''Para sair digite 1
Aperte qualquer tecla para o jogo continuar!''')

while(inicio != '1'):
	jogada += 1
	inicio = input()
	if inicio == '1':
		print('Jogo encerrado')
	else:
		valor = random.randint(2, 12)
		print('Valor do dado: {}'.format(valor))
		if jogada == 1:
			if valor == 7 or valor == 11:
				print('Você conseguiu um natural, PARABÉNS!!!')
				pass
			elif valor == 2 or valor == 3 or valor == 12:
				print('Craps, não desanime tente outra vez!')
				pass
			else:
				pontos = valor
				pass
		else:
			if valor == 7:
				print('Você não conseguiu seu ponto a tempo e isso te leva ao THE END!')
				pass
			elif pontos == valor:
				print('Você conseguiu, PARABÉNS!!!')
				pass