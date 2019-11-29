def validacao(arquivo):
    with open(arquivo) as lista:
        with open('saida6_invalidos.txt', 'w') as invalido:
            with open( 'saida6_validos.txt', 'w') as valido:
                for linha in lista:
                    linha_quebrada =  linha.strip('\n').strip('[]').split('.')
                    if linha_quebrada[0] == '0':
                        junto = '.'.join(linha_quebrada)
                        print(junto, file=invalido)
                    elif linha_quebrada[0] != '0':
                        junto = '.'.join(linha_quebrada)
                        print(junto, file=valido)

validacao('ips.txt')