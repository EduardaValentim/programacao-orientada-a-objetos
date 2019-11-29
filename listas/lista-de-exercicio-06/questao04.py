def media(aluno, nota_arq):
    lista_nota = []
    lista_nome = []
    incrementa_nome = 0
    incrementa_nota = 0
    
    with open(nota_arq) as nota:
        for escrever_nota in nota:
            notas = escrever_nota.split()
            nota1 = float(notas[0])
            nota2 = float(notas[1])
            nota3 = float(notas[2])
            nota4 = float(notas[3])
            lista_nota.append((nota1 + nota2 + nota3 + nota4) / 4)
    with open(aluno) as nome:
        with open('saida4_media.txt', 'w') as media:
            for escrever_nome in nome:
                lista_nome.append(escrever_nome.strip('\n'))
                print('{}, {:.1f}'.format(lista_nome[incrementa_nome], lista_nota[incrementa_nota]), file=media)
                incrementa_nome += 1
                incrementa_nota +=1

media('saida4_alunos.txt', 'saida4_notas.txt')