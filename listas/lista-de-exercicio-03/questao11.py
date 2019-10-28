salario = float(input('Digite o valor do seu salário: R$'))
if salario <= 280:
	salario_novo = (salario * 0.2) + salario
	print('Salário antes do reajuste R${:.2f}'.format(salario))
	print('Aumento de 20%')
	print('20% do seu salário resulta em {:.2f}'.format(salario * 0.2))
	print('Seu salário atual é R${:.2f}'.format(salario_novo))
elif 280 < salario <= 700:
	salario_novo = (salario * 0.15) + salario
	print('Salário antes do reajuste R${:.2f}'.format(salario))
	print('Aumento de 15%')
	print('15% do seu salário resulta em {:.2f}'.format(salario * 0.15))
	print('Seu salário atual é R${:.2f}'.format(salario_novo))
elif 700 < salario <= 1500:
	salario_novo = (salario * 0.1) + salario
	print('Salário antes do reajuste R${:.2f}'.format(salario))
	print('Aumento de 10%')
	print('10% do seu salário resulta em {:.2f}'.format(salario * 0.1))
	print('Seu salário atual é R${:.2f}'.format(salario_novo))
elif 1500 < salario:
	salario_novo = (salario * 0.05) + salario
	print('Salário antes do reajuste R${:.2f}'.format(salario))
	print('Aumento de 5%')
	print('5% do seu salário resulta em {:.2f}'.format(salario * 0.05))
	print('Seu salário atual é R${:.2f}'.format(salario_novo))
else:
	print('Valor inválido!')