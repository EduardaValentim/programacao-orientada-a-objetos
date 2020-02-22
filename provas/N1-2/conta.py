import datetime
class Conta:
	def __init__(self, numero, cliente, saldo, limite=1000):
		self.numero = numero
		self.cliente = cliente
		self.saldo = saldo
		self.limite = limite
		self.historico = Historico()

	def deposita(self, valor):
		self.saldo += valor
		self.historico.transacoes.append('Deposito de {}'.format(valor))

	def saca(self, valor):
		if self.saldo < valor:
			return False
		else:
			self.saldo -= valor
			self.historico.transacoes.append('Saque de {}'.format(valor))
			return True 

	def extrato(self):
		print('Número: {} \nCliente: {}'.format(self.numero, self.cliente))
		self.historico.transacoes.append('Tirou extrato \n\t\tSaldo de {}'.format(self.saldo))

	def transfere_para(self, destino, valor):
		retirou = self.saca(valor)
		if retirou == False:
			return False
		else:
			destino.deposita(valor)
			self.historico.transacoes.append('Transferência de {} para conta {}'.format(valor, destino.numero))
			return True

class Cliente:
	def __init__(self, nome, sobrenome, cpf):
		self.nome = nome
		self.sobrenome = sobrenome
		self.cpf = cpf

	def __str__(self):
		return '{} {} \nCPF: {}'.format(self.nome, self.sobrenome, self.cpf)

class Historico:
	def __init__(self):
		self.data_abertura = datetime.datetime.today()
		self.transacoes = []

	def imprimir(self):
		print('Data de abertura: {}'.format(self.data_abertura))
		print('Transações: ')
		for t in self.transacoes:
			print('-', t)


"""				INSTANCIANDO				"""
cliente1 = Cliente('Dudah', 'Valentim', '123.456.765-98')
cliente2 = Cliente('Cris', 'Januário', '987.654.321-10')
conta1 = Conta('123-7', cliente1, 3000)
conta2 = Conta('987-2', cliente2, 40000)
conta1.deposita(5000)
conta1.deposita(5000)
conta1.saca(500.86)
conta1.transfere_para(conta2, 250)
conta1.extrato()
conta1.historico.imprimir()
print(' ')
conta2.extrato()
conta2.historico.imprimir()