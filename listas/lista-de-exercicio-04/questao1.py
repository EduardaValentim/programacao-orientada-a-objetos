# Variáveis para a item 1
a = []
a_sem_ponto = []
item1 = []

# Variáveis para a item 2
item2 = []

# Variáveis para a item 3
c = []
c_sem_ponto = []
item3 = []

# Variáveis para a item 4
d = []
d_sem_ponto = []
item4 = []

# Leitura do arquivo

arquivo = open('amazon.csv', 'r')
for linha in arquivo:
	dados = linha.strip('\n').split(',')

	# Manipulação de dados

	if dados[0] == '2015' and dados[1] == '"Acre"':
		a = dados[3]
		str(a)
		a_sem_ponto = a.replace('.', '')
		a_inteiro = int(a_sem_ponto)
		item1.append(a_inteiro)

	elif dados[0] == '2014' and dados[1] == '"Ceara"':
		passando_para_int = int(dados[3])
		item2.append(passando_para_int)

	elif dados[1] == '"Amazonas"':
		c = dados[3]
		str(c)
		c_sem_ponto = c.replace('.', '')
		c_inteiro = int(c_sem_ponto)
		item3.append(c_inteiro)

	if dados[0] == ('2010' and '2011' and '2012' and '2013' and '2014' and '2015' and '2016' and '2017') and dados[1] == '"Mato Grosso"':
		d = dados[3]
		str(d)
		d_sem_ponto = d.replace('.', '')
		d_inteiro = int(d_sem_ponto)
		item4.append(d_inteiro)


# exibição dos dados manipulados

print('Em 2015 ocorreram {} queimadas no Estado do Acre.'.format(sum(item1)))
print('Em 2014 ocorreram {} queimadas no Estado do Ceará.'.format(sum(item2)))
print('No Estado do Amazonas ocorreram {} queimadas, de 1998 a 2017.'.format(sum(item3)))
print('No Estado do Mato Grosso ocorreram {} queimadas, de 2010 a 2017.'.format(sum(item4)))
arquivo.close()