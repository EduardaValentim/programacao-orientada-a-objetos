import random 
nomes = ['Eduarda', 'Edson', 'Josefa', 'Francisco', 'Iara', 'Lucas', 'Maria', 'Vanessa', 'Clara', 'Pedro', 'Debora', 'Carlos', 'Joao', 'Clarice', 'Tiago', 'Marcos', 'Marcelo', 'Fernana', 'Fernando', 'Brenda']
sobrenomes = ['Alencar', 'Valentim', 'Silva', 'Bezerra', 'Belli', 'Costa', 'Farias', 'Fernadez', 'Fontes', 'Facundes', 'Lemos', 'Marques', 'Mendes', 'Nascimento', 'Nogueira', 'Oliveira', 'Pacheco', 'Parent', 'Penna', 'Peixoto']

tamanho_da_lista = int(input('Qual o tamanho da lista? '))
inicio = 1
with open('saida2.txt', 'w') as saida:
    while inicio <= tamanho_da_lista:
        inicio += 1
        nome = nomes[random.randint(0, 19)]
        sobrenome = sobrenomes[random.randint(0, 19)]
        idade = random.randint(1, 101)
        altura = random.randint(20, 200)
        print('{} {} com {} ano(s) e {} cm'.format(nome, sobrenome, idade, altura), file=saida)
