c = []
c_sem_ponto = []
questao3 = []

arquivo = open('amazon.csv', 'r')
for linha in arquivo:
	dados = linha.strip('\n').split(',')
	if dados[1] == '"Amazonas"':
		c = dados[3]
		str(c)
		c_sem_ponto = c.replace('.', '')
		c_inteiro = int(c_sem_ponto)
		questao3.append(c_inteiro)
print(questao3)
print(sum(questao3))
arquivo.close()