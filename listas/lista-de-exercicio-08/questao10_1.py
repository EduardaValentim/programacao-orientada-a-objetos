class Diario:
    def __init__(self, nome='Querido Diario', folhas=[], caneta=50):
        self.nome = nome
        self.folhas = []
        self.caneta = 50
        print(nome)
    
    def escrever(self, frase):
        if len(frase) > self.caneta:
            return print('Sua caneta não tem tinta o sufuciente para escrever essa frase \nTente uma frase menor!')
        else:
            self.folhas.append(frase)
            self.caneta -= len(frase)
            return self.folhas and self.caneta

    def mostrar_caneta(self):
        return print(self.caneta)

    def encher_caneta(self):
        self.caneta = 50
        return self.caneta

    def apagar_folha(self, folha):
        inverter_indice_lista = folha - 1
        self.folhas.remove(self.folhas[inverter_indice_lista])
        return self.folhas

    def mostrar_folha(self, pagina):
        inverter_indice_lista = pagina - 1
        return print(self.folhas[inverter_indice_lista])

dia = Diario()
dia.escrever('vidaaaa')
dia.mostrar_caneta()
dia.encher_caneta()
dia.escrever('tentando concertar')
dia.mostrar_caneta()
dia.mostrar_folha(1)
dia.mostrar_folha(2)
dia.apagar_folha(1)
dia.mostrar_folha(1)
dia.encher_caneta()
dia.mostrar_caneta()