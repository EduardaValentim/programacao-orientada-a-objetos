def alterar_bytes(numero):
    resultado = numero / 1024 / 1024
    return resultado
def porcentagem(mega):
    resultado = 100 * mega / 2581.56
    return resultado

soma = 0
numero_usuario = 1
with open('usuarios.txt') as dados:
    with open('relatorio.txt', 'w') as escrever:
        print('ACME Inc.        Uso do espaço em disco pelos usuários', file=escrever)
        print('--'*28, file=escrever)
        print('{:<3}   {:<10}   {:<17}     {:<9}'.format('Nr.', 'Usuário', 'Espaço utilizado', '% do uso'), file=escrever)
        print(' ', file=escrever)
        for linha in dados:
            linha_quebrada = linha.strip().split(' ')
            mega = alterar_bytes(int(linha_quebrada[1]))
            print('{:<3}   {:<10}    {:>10.2f} MB      {:>9.2f}%'.format(numero_usuario, linha_quebrada[0], mega, porcentagem(mega)),file=escrever)
            numero_usuario += 1
            soma += mega
        print(' ', file=escrever)
        print('Espaço total ocupado: {:.2f} MB'.format(soma), file=escrever)  
        print('Espaço médio ocupado: {:.2f} MB'.format(soma/numero_usuario), file=escrever)   
