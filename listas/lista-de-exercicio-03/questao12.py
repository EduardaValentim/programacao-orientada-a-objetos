def imposto_renda(salario):
	if salario <= 900:
		imposto = 0
		return imposto
	elif 900 < salario <= 1500:
		imposto = salario * 0.05
		return imposto
	elif 1500 < salario <= 2500:
		imposto = salario * 0.1
		return imposto
	elif 2500 < salario:
		imposto = salario * 0.2
		return imposto

def porcentagem(ganho):
	if ganho <= 900:
		salario = 0
		return salario
	elif 900 < ganho <= 1500:
		salario = 5
		return salario
	elif 1500 < ganho <= 2500:
		salario = 10
		return salario
	elif 2500 < ganho:
		salario = 20
		return salario

valor_hora = float(input('Digite o valor da hora trabalhada: '))
hora_trabalhada = float(input('digite quantas horas você trabalhou no mês: '))
salario = valor_hora * hora_trabalhada
porcento = porcentagem(salario)
imposto = imposto_renda(salario)


print('Salário Bruto:      : R$ {:.2f}'.format(valor_hora, hora_trabalhada, salario))
print('(-) IR ({}%)         : R$ {:.2f}'.format(porcento, imposto))
print('(-) INSS (3%)       : R$ {:.2f}'.format(0.03 * salario))
print('FGTS (11%)          : R$ {:.2f}'.format(0.11 * salario))
print('Total de descontos  : R$ {:.2f}'.format(imposto + (0.03 * salario)))
print('Salário Liquido     : R$ {:.2f}'.format(salario - imposto - (0.03 * salario)))