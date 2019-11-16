def somaImposto(taxaImposto, custo):
	porcentagem = taxaImposto / 100
	custo_novo = custo + (porcentagem * custo)
	return custo_novo

imposto = int(input('Qual a porcentagem do Imposto? '))
produto = float(input('Qual o valor do produto? '))
print('O produto que custava R${:.2f}'.format(produto), end='')
print(' passará a valer R${:.2f} com Imposto.'.format(somaImposto(imposto, produto)))