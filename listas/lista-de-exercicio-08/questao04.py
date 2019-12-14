class Caneta:
    def __init__(self, cor, marca, numero_ponta, volume_tinta):
        self.cor = cor
        self.marca = marca
        self.numero_ponta = numero_ponta
        self.volume_tinta = 50
    
    def encher_caneta(self):
        self.volume_tinta = 50
        return print(self.volume_tinta)
    
    def escrever(self, palavras):
        self.volume_tinta = self.volume_tinta - len(palavras.strip())
        return print(self.volume_tinta)

    def retornar_marca(self):
        return print(self.marca)

    def imprimir_caracteristicas(self):
        return print(self.cor, '\n', self.marca, '\n', self.numero_ponta, '\n', self.volume_tinta)
        
ca1 = Caneta('azul', 'bic', 0.7, 50)
ca1.retornar_marca()
ca1.escrever('coisa complicada')
ca1.encher_caneta()
ca1.imprimir_caracteristicas()