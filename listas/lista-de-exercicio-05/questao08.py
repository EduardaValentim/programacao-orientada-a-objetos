def contar_digitos(num):
	soma = len(num)
	return soma
num = str(input('Digite um número inteiro: ')).strip()
print('Esse número contém {} dígitos'.format(contar_digitos(num)))
