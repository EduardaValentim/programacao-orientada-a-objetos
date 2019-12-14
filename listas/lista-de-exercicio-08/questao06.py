class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor_lado(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b
    
    def retornar_valor_lado(self):
        return self.lado_a and self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return self.lado_a * 2 + self.lado_b * 2

r1 = Retangulo(2, 3)
r1.calcular_area()
r1.calcular_perimetro()
r1.mudar_valor_lado(4, 5)
r1.retornar_valor_lado()
r1.calcular_area()
r1.calcular_perimetro()