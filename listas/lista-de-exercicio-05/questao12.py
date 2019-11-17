def embaralhar(palavra):
	import random
	palavra_embaralhar = random.sample(palavra,len(palavra))
	palavra_embaralhada = ''.join(palavra_embaralhar)
	return palavra_embaralhada

palavra = str(input('Qual palavra você deseja embaralhar? ')).strip().upper()
print(embaralhar(palavra))