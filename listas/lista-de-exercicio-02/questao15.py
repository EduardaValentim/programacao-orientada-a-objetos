valor_hora = float(input('Quanto você ganha por hora? '))
hora_mes = float(input('Quantas horas você trabalha por mês? '))

salario_bruto = valor_hora * hora_mes
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
desconto_total = ir + inss + sindicato
salario_liquido = salario_bruto - desconto_total

print('+ Salário Bruto   : R${:.2f}'.format(salario_bruto))
print('- IR (11%)        : R${:.2f}'.format(ir))
print('- INSS (8%)       : R${:.2f}'.format(inss))
print('- Sindicato (5%)  : R${:.2f}'.format(sindicato))
print('= Salário Liquido : R${:.2f}'.format(salario_liquido))