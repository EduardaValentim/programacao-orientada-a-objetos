def alterar_nota(arquivo, nome, nota_atual):
    with open(arquivo) as mudar:
        for linha in mudar:
            quebra_linha = linha.split()
            print(quebra_linha)

                #print('{:.1f}'.format(nota_atual), file=mudar)
alterar_nota('saida4_media.txt', 'Debora Peixoto', 6.0)