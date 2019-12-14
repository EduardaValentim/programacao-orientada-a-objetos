class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        print(self.cor, self.circunferencia, self.material)

    def trocarCor(self, cor):
        self.cor = cor
        return self.cor
        
    def mostrarCor(self):
        return print(self.cor)

b1 = Bola('azul', 4, 'papel')
b1.trocarCor('vermelho')
b1.mostrarCor()