questao2 = []

arquivo = open('amazon.csv', 'r')
for linha in arquivo:
	dados = linha.strip('\n').split(',')
	if dados[0] == '2014' and dados[1] == '"Ceara"':
		passando_para_int = int(dados[3])
		questao2.append(passando_para_int)
print(questao2)
print(sum(questao2))
arquivo.close()