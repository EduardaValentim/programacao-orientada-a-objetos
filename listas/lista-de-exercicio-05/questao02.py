def enesima(num):
    lista = []
    while num not in lista:
    	for numero in range(1, n + 1):
    		lista.append(numero)
    		tira_colchete = str(lista).strip('[]').replace(',', '')
    		print(tira_colchete)

n = int(input('digite um número: '))
enesima(n)