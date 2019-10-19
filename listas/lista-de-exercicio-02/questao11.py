numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite mais um número inteiro: '))
numero3 = float(input('Digite um número real: '))

calculo1 = (numero1 * 2) * numero2
calculo2 = (numero1 * 3) + numero3
calculo3 = numero3 ** 3

print('O produto do dobro de {} com {} resulta em {}!'.format(numero1, numero2, calculo1))
print('A soma do triplo de {} com {:.2f} resulta em {:.2f}!'.format(numero1, numero3, calculo2))
print('O numero {:.2f} elevado ao cubo resulta em {:.2f}!'.format(numero3, calculo3))