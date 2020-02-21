def criar_conta(numero, titular, saldo, limite):
	conta = {'Número:': numero, 'Títular;': titular, 'Saldo:': saldo, 'Limite:': limite}
	return conta

def deposita(conta, valor):
	conta['Saldo:'] += valor
	return conta

def saca(conta, valor):
	conta['Saldo:'] -= valor
	return conta

def extrato(conta):
	return print('Número: {} \nSaldo: {}'.format(conta['Número:'], conta['Saldo:']))

