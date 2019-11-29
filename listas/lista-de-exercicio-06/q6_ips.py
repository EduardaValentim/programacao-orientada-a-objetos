import random
lista = []
ips = []
for x in range(1, 1000):
    um = 0
    dois = random.randint(0, 255)
    tres = random.randint(0, 255)
    quatro = random.randint(0, 255)
    lista.append(um)
    lista.append(dois)
    lista.append(tres)
    lista.append(quatro)
with open('ips.txt', 'w') as numero:
    for y in range(1, 1000):
        print('{}.{}.{}.{}'.format(lista[random.randint(1, 50)], lista[random.randint(1, 50)], lista[random.randint(1, 50)], lista[random.randint(1, 50)]), file=numero) 
