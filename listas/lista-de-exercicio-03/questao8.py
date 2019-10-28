produto1 = float(input('Qual o preço do primeiro produto? '))
produto2 = float(input('Qual o preço do segundo produto? '))
produto3 = float(input('Qual o preço do terceiro produto? '))

lista = [produto1, produto2, produto3]

print('Você deve comprar o produto que custa R${}'.format(min(lista)))