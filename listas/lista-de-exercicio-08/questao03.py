class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2

qua1 = Quadrado(2)
qua1.calcular_area()
qua1.mudar_valor_lado(4)
mostrar = qua1.calcular_area()
print(mostrar)