def manha_noite(hora_str):
	separacao = hora_str.split(':')
	separar = int(separacao[0])
	if separar == 00:
		registro = 'P'
		return registro
	elif separar >= 12:
		registro = 'P'
		return registro
	elif 0 < separar < 12:
		registro = 'A'
		return registro

def conversao(hora_str):
	separacao = hora_str.split(':')
	if separacao[0] == '13':
		separacao[0] = '1'
		return separacao
	elif separacao[0] == '14':
		separacao[0] = '2'
		return separacao
	elif separacao[0] == '15':
		separacao[0] = '3'
		return separacao
	elif separacao[0] == '16':
		separacao[0] = '4'
		return separacao
	elif separacao[0] == '17':
		separacao[0] = '5'
		return separacao
	elif separacao[0] == '18':
		separacao[0] = '6'
		return separacao
	elif separacao[0] == '19':
		separacao[0] = 7
		return separacao
	elif separacao[0] == '20':
		separacao[0] = 8
		return separacao
	elif separacao[0] == '21':
		separacao[0] = 9
		return separacao
	elif separacao[0] == '22':
		separacao[0] = '10'
		return separacao
	elif separacao[0] == '23':
		separacao[0] = '11'
		return separacao
	elif separacao[0] == '00':
		separacao[0] = '12'
		return separacao
	else:
		return separacao

hora = str(input('Digite a hora escolhida: ')).strip()
turno = manha_noite(hora)
converter = conversao(hora)
print('São {}:{} {}.'.format(converter[0], converter[1], turno))
print('''Deseja outra vez?
[ 1 ] SIM
[ 2 ] NÃO''')
opcao = int(input())

while opcao == 1:
	hora = str(input('Digite a hora escolhida: ')).strip()
	turno = manha_noite(hora)
	converter = conversao(hora)
	print('São {}:{} {}.'.format(converter[0], converter[1], turno))
	print('''Deseja outra vez?
[ 1 ] SIM
[ 2 ] NÃO''')
	opcao = int(input())