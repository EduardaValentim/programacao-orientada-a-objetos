class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        nova = self.velocidade_atual + delta
        if nova <= self.velocidade_maxima:
            self.velocidade_atual = nova
        else:
            self.velocidade_atual = 180
        return self.velocidade_atual
            
    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        if nova > 0:
            self.velocidade_atual = nova
        else:
            self.velocidade_atual = 0
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(20))
