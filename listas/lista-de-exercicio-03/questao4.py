vogais = ('a', 'e', 'i', 'o', 'u')
consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

letra = str(input('Qual letra quer verificar? ')).lower()

print('Essa letra é vogal?')
print(letra in vogais)
print('Essa letra é consoante?')
print(letra in consoantes)