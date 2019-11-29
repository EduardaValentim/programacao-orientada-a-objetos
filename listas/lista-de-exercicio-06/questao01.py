import random 
nomes = ['Eduarda', 'Edson', 'Josefa', 'Francisco', 'Iara', 'Lucas', 'Maria', 'Vanessa', 'Clara', 'Pedro', 'Debora', 'Carlos', 'Joao', 'Clarice', 'Tiago', 'Marcos', 'Marcelo', 'Fernana', 'Fernando', 'Brenda']
sobrenomes = ['Alencar', 'Valentim', 'Silva', 'Bezerra', 'Belli', 'Costa', 'Farias', 'Fernadez', 'Fontes', 'Facundes', 'Lemos', 'Marques', 'Mendes', 'Nascimento', 'Nogueira', 'Oliveira', 'Pacheco', 'Parent', 'Penna', 'Peixoto']

tamanho_da_lista = int(input('Qual o tamanho da lista? '))
inicio = 1
with open('saida1.txt', 'w') as saida:
    while inicio <= tamanho_da_lista:
        inicio += 1
        nome = nomes[random.randint(0, 20)]
        sobrenome = sobrenomes[random.randint(0, 20)]
        idade = random.randint(1, 101)
        print(nome, sobrenome, idade, file=saida)
