class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def __str__(self):
    return f'{self.nome} tem {self.idade} ano(s)'

  def is_adulto(self):
    if self.idade < 18:
      return False
    else:
      return True

class Vendedor(Pessoa):
  def __init__(self, nome, idade, salario):
    super().__init__(nome, idade)
    self.salario = salario
  
class Cliente(Pessoa):
  def __init__(self, nome, idade):
    super().__init__(nome, idade)
    self.compras = []

  def registrar_compra(self, compra):
    return self.compras.append(compra)

  def get_data_ultima_compra(self):
    return self.compras[-1]

  def total_compras(self):
    soma = 0
    for x in self.compras:
      soma += x.valor
    return f'{soma}'

from datetime import datetime
class Compra:
  def __init__(self, vendedor, data, valor):
    self.vendedor = vendedor.nome
    self.data = datetime.now()
    self.valor = valor

  def __str__(self):
    return 'Vendedor: {} \nData: {} \nValor: {:.2f}'.format(self.vendedor, self.data, self.valor)

##################################
##################################
def main():
  p1 = Pessoa('Eduarda', 21)
  p2 = Vendedor('Cristina', 22, 999)
  p3 = Cliente('Dudah', 23)
  c1 = Compra(p2, 'hoje', 4)
  c2 = Compra(p2, 'hoje', 4)
  c3 = Compra(p2, 'hoje', 4)
  c4 = Compra(p2, 'hoje', 4)
  c5 = Compra(p2, 'hoje', 4)
  c6 = Compra(p2, 'hoje', 4)
  c7 = Compra(p2, 'hoje', 5)
 
 
  
  print('Testando primeira classe e seus métodos')
  print('\t', p1)
  print('\t', p1.is_adulto())
  print('\t', type(p1))
  print('Final do teste.')

  print(' ')

  print('Testando segunda classe e seus métodos')
  print('\t', p2)
  print('\t', type(p2))
  print('Final do teste.')

  print(' ')

  print('Testando terceira classe e seus métodos')
  print('\t', p3)
  print('\t', type(p3))
  p3.registrar_compra(c1)
  p3.registrar_compra(c2)
  p3.registrar_compra(c3)
  p3.registrar_compra(c4)
  p3.registrar_compra(c5)
  p3.registrar_compra(c6)
  p3.registrar_compra(c7)
  print('\tTotal de compras: R$', p3.total_compras())
  print('\tÚltima compra: \n', p3.get_data_ultima_compra())
  print('Final do teste.')

  print(' ')

  print('Testando quarta classe e seus métodos')
  print(c1)
  print('Final do teste.')
  
  

if __name__=='__main__':
  main()