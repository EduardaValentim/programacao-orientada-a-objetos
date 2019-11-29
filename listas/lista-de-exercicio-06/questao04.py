def media(aluno, nota_arq):
    with open(nota_arq) as nota:
        with open(aluno) as nome:
            with open('saida4_media.txt', 'w') as media:
                for escrever_nome in nome:
                    for escrever_nota in nota:
                        notas = escrever_nota.split()
                        nota1 = float(notas[0])
                        nota2 = float(notas[1])
                        nota3 = float(notas[2])
                        nota4 = float(notas[3])
                        medias = (nota1 + nota2 + nota3 + nota4) /4
                        print('{}'.format(escrever_nome), file=media, end='')
                        print('{:.1f}'.format(medias), file=media)
                        break
                        
                        
media('saida4_alunos.txt', 'saida4_notas.txt')