class Tv:
    def __init__(self, tela, canal, controle, volume):
        self.tela  = tela
        self.canal = 1
        self.controle = controle
        self.volume = 0

    def mostrarCanal(self):
        return print(self.canal)
    
    def mudarCanalAumentar(self):
        if 0 < self.canal < 100:
            self.canal += 1
            return self.canal
        elif self.canal == 100:
            self.canal = 1
            return self.canal 

    def mudarCanalDiminuir(self):
        if 1 < self.canal <= 100:
            self.canal -= 1
            return self.canal
        elif self.canal == 1:
            self.canal = 100
            return self.canal 

    def aumentarVolume(self):
        if self.volume <= 30:
            self.volume += 1
            return self.volume
        elif self.volume > 30:
            return print('Limite excedido')

    def diminuirVolume(self):
        if 0 > self.volume <= 30:
            self.volume -= 1
            return self.volume
        elif self.volume == 0:
            return print('Mudo')