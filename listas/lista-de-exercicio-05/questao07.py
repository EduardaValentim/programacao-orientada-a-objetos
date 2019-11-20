def valorPagamneto(valor, dias):
	if dias == 0:
		return valor
	else:
		multa = valor + (valor * 0.03) 
		juros = dias * 0.001
		valor_novo = multa + juros
		return valor_novo

relatorio = []

valor_prestacao = float(input('Qual o valor da prestação? '))
dias_atraso = int(input('Quantos dias essa prestação está em atraso? '))
print('O valor a ser pago será R${:.2f}'.format(valorPagamneto(valor_prestacao, dias_atraso)))
relatorio.append(valorPagamneto(valor_prestacao, dias_atraso))

# Loop
while valor_prestacao != 0:
	valor_prestacao = float(input('Qual o valor da prestação? '))
	dias_atraso = int(input('Quantos dias essa prestação está em atraso? '))
	print('O valor a ser pago será R${:.2f}'.format(valorPagamneto(valor_prestacao, dias_atraso)))
	relatorio.append(valorPagamneto(valor_prestacao, dias_atraso))

# relatório
print('\n')
print('{:^15}'.format('RELATÓRIO DO DIA'))
print('Foram pagas {} prestações'.format(len(relatorio) - 1))
print('O valor total das prestações: R${:.2f}'.format(sum(relatorio)))

"""
preciso saber a diferença entre ENCERRAR o programa e não GERAR MULTA.
"""