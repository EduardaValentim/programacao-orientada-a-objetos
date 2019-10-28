n1 = float(input('Digite um  número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

lista = [n1, n2, n3]
lista_decrescente = sorted(lista, reverse=True) 

print(lista_decrescente)