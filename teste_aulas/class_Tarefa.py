from datetime import datetime
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
    
    def concluir(self):
        self.feito = True
    
    def __str__(self):
        imprimir = 'Data:' + str(self.criacao) + '\nDescrição:' + self.descricao + '\nStatus' + str(self.feito)
        return imprimir

def main():
    casa = []
    t1 = Tarefa('Lavar os pratos.')
    t2 = Tarefa('Lavar os pratos.')
    print(t1)

if __name__ =='__main__':
    main()