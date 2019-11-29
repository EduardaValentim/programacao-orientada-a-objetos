def alterar_nota(arquivo, nome, nota_atual):
    with open(arquivo) as mudar:
        with open('saida5.txt', 'w') as sub_escrever:
            for linha in mudar:
                quebra_linha = linha.strip('\n').split(',')
                if quebra_linha[0] != nome:
                   linha_perf = ' '.join(quebra_linha) 
                   print(linha_perf, file=sub_escrever)
                elif quebra_linha[0] == nome:
                    quebra_linha[1] = str(nota_atual)
                    linha_perf = ' '.join(quebra_linha)
                    print(linha_perf, file=sub_escrever)

alterar_nota('saida4_media.txt', 'Debora Parent', 7.0)