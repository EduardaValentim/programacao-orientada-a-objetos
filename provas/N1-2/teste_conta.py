def criar_conta(numero, titular, saldo, limite):
	conta = {'Número:': numero, 'Titular:': titular, 'Saldo:': saldo, 'Limite:': limite}
	return conta

def deposita(conta, valor):
	conta['Saldo'] += valor

def saca(conta, valor):
	conta['Saldo'] -= valor

def extrato(conta):
	return print('Número: {} \nSaldo: {}'.format(conta['Número:'], conta['Saldo:']))
