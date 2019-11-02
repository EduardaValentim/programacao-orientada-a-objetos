d = []
d_sem_ponto = []
questao4 = []

arquivo = open('amazon.csv', 'r')
for linha in arquivo:
	dados = linha.strip('\n').split(',')
	if dados[0] == ('2010' and '2011' and '2012' and '2013' and '2014' and '2015' and '2016' and '2017') and dados[1] == '"Mato Grosso do Sul"':
		d = dados[3]
		str(d)
		d_sem_ponto = d.replace('.', '')
		d_inteiro = int(d_sem_ponto)
		questao4.append(d_inteiro)
print(questao4)
print(sum(questao4))
arquivo.close()