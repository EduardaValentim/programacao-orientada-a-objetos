a = float(input('Qual o comprimento da primeira reta? '))
b = float(input('Qual o comprimento da segunta reta? '))
c = float(input('Digite o comprimento da terceiraa reta? '))

if((b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b):
    print('Essas retas FORMAM um triângulo!')
    if a == b == c:
    	print('Um triângulo EQUILÁTERO!')
    elif(a == b != c) or (a == c != b) or (b == c != a):
    	print('Um triângulo ISÓSCELES!')
    elif a != b != c:
    	print('Um triângulo ESCALENO!')  
else:
    print('Essas retas NÃO FORMAM um triângulo!')