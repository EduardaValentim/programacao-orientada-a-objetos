peso = float(input('Digite a quantidade de Kg de peixe: '))
excesso = peso - 50
multa = excesso * 4

if peso > 50:
	print('Você irá pagar uma multa de R${:.2f} por exceder {}Kg além do permitido!'.format(multa, excesso))
else:
	print('Parabéns! Você não excedeu o limite diário.')