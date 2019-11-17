def extenso(data):
	if data[1] == '01':
		data[1] = 'Janeiro'
		return data
	elif data[1] == '02':
		data[1] = 'Fevereiro'
		return data
	elif data[1] == '03':
		data[1] = 'Março'
		return data
	elif data[1] == '04':
		data[1] = 'Abril'
		return data
	elif data[1] == '05':
		data[1] = 'Maio'
		return data
	elif data[1] == '06':
		data[1] = 'Junho'
		return data
	elif data[1] == '07':
		data[1] = 'Julho'
		return data
	elif data[1] == '08':
		data[1] = 'Agosto'
		return data
	elif data[1] == '09':
		data[1] = 'Setembro'
		return data
	elif data[1] == '10':
		data[1] = 'Outubro'
		return data
	elif data[1] == '11':
		data[1] = 'Novembro'
		return data
	elif data[1] == '12':
		data[1] = 'Dezembro'
		return data
	else:
		data = 'Formato Inválido'

print('''Passando o mês para extenso
digite a data:
Ex: 01/01/2001''')
data = str(input()).strip().split('/')
data_extenso = extenso(data)
print('{} de {} de {}'.format(data_extenso[0], data_extenso[1], data_extenso[2]))