def vogal(letra):
	if letra == 'a' or 'e' or 'i' or 'o' or 'u':
		return True
	else:
		return False
def consoante(letra):
	if letra == 'a' or 'e' or 'i'  or 'o' or 'u':
		return False
	else:
		return True

letra = str(input('Qual letra? ')).lower()
print('Essa letra é vogal?')
print(vogal(letra))
print('Essa letra é consoante?')
print(consoante(letra))