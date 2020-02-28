class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    self.adulto = False

  def __str__(self):
    return f'{self.nome} tem {self.idade} ano(s)!'

  def is_adulto(self):
    self.adulto = True

class Vendedor(Pessoa):
  def __init__(self, nome, idade, salario):
    super().__init__(nome, idade)
    self.salario = salario

from datetime import datetime
class Cliente(Pessoa):
  def __init__(self, nome, idade):
    super().__init__(nome, idade)
    self.data_compra = datetime.now()
    self.compras = []

  def __str__(self):
    return f'{self.nome} tem {self.idade} ano(s)!'

  def __iter__(self):
    return self.compras.__iter__()

  def registrar_compra(self, compra, valor):
    self.compras.append(f'{self.data_compra}  {compra} R$ {valor}')

  def get_data_ultima_compra(self):
    self.compras[-1]

  def total_compras(self):
    soma = []
    for x in self.compras:
      x_break = x.split()
      x_flo = float(x_break[4])
      soma.append(x_flo)
    for x in self.compras:
      print(x)
    return f'total: {sum(soma)}'

class Compra:
  def __init__(self, vendedor, data, valor):
    self.vendedor = Vendedor
    self.data = datetime.now()
    self.valor = valor

  def __str__(self):
    return f'Vendedor: {self.vendedor}\nData de compra: {self.data}\nValor da compra: {self.valor}'

print('Testando primeira classe e seus métodos')
pessoa = Pessoa('Eduarda Valentim', 21)
print('\t', pessoa)
print('\t', pessoa.is_adulto())
print('\t', type(pessoa))
print('Final do teste.')

print(' ')

print('Testando segunda classe e seus métodos')
vendedor = Vendedor('Cristina Januário', 25, 1000)
print('\t', vendedor)
print('\t', type(vendedor))
print('Final do teste.')

print(' ')

print('Testando terceira classe e seus métodos')
cliente = Cliente('Dudah', 20)
print(cliente)
cliente.registrar_compra('maça',2)
cliente.registrar_compra('uva',3)
cliente.registrar_compra('suco',4)
print(cliente.total_compras())
print(cliente.get_data_ultima_compra())
print('Final do teste.')

print(' ')

print('Testando quarta classe e seus métodos')
compra = Compra('Cris', 'hoje', 4.50)
print(compra)
print('Final do teste.')
