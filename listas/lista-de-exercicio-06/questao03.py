def copiar(texto1, texto2):
    with open(texto1, 'r') as leitura:
        with open(texto2, 'w') as escrita:
            for linha in leitura:
                linha_formatada = linha.strip('\n')
                if '//' not in linha_formatada:
                   print(linha_formatada, file=escrita)

copiar('saida1.txt', 'saida3.txt')
