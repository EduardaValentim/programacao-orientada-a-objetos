from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def procurar(self, descricao):
        for tarefa in self.tarefas:
            if tarefa.descricao == descricao:
                return tarefa
    
    def pendentes(self):
        tarefas_pendentes = []
        for tarefa in self.tarefas:
            if tarefa.feito == False:
                tarefas_pendentes.append(tarefa)
        return tarefas_pendentes
            
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
    
    def concluir(self):
        self.feito = True
    
    def __str__(self):
        imprimir = 'Data: ' + str(self.criacao) + '\nDescricao: ' + self.descricao + '\nStatus: ' + str(self.feito)
        return imprimir

def main():
    '''
    casa = []
    t1 = Tarefa('Lavar os pratos.')
    t2 = Tarefa('Lavar roupa.')
    t3 = Tarefa('Escovar os dentes.')

    casa.append(t1)
    casa.append(t2)
    casa.append(t3)

    for tarefa in casa:
        if tarefa.descricao == 'Lavar roupa.':
            tarefa.concluir()
    
    for tarefa in casa:
        print(tarefa)
        print('\n')
    '''
    casa = Projeto('Tarefas de casa')

    casa.adicionar('Lavar os pratos.')
    casa.adicionar('Lavar roupa.')
    casa.adicionar('Escovar os dentes.')

    casa.procurar('Escovar os dentes.').concluir()
    for tarefa in casa.pendentes():
        print(tarefa)
        print('\n')

if __name__ =='__main__':
    main()