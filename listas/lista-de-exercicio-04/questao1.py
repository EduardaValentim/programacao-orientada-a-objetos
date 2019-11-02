a = []
a_sem_ponto = []
questao1 = []

arquivo = open('amazon.csv', 'r')
for linha in arquivo:
	dados = linha.strip('\n').split(',')
	if dados[0] == '2015' and dados[1] == '"Acre"':
		a = dados[3]
		str(a)
		a_sem_ponto = a.replace('.', '')
		a_inteiro = int(a_sem_ponto)
		questao1.append(a_inteiro)
print(questao1)
print(sum(questao1))
arquivo.close()