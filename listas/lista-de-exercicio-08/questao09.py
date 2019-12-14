class Macaco:
    def __init__(self, nome, bucho=[]):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
        return self.bucho

    def ver_bucho(self):
        return print(self.bucho)

    def digerir(self):
        self.bucho.remove(self.bucho[0])
        return self.bucho

mac1 = Macaco('Mac1')
mac1.comer('amora')
mac1.comer('pera')
mac1.comer('uva')
mac1.digerir()
mac1.ver_bucho()

mac2 = Macaco('Mac2')
mac2.comer('pera')
mac2.comer('uva')
mac2.comer(mac1)
mac2.digerir()
mac2.ver_bucho()

'''
Sim é possível criar um macaco canibal, mas por incrível que pareça o
Mac1 continua vivo no estômago do Mac2.
O suco gástrico do Mac2 necessita de reparos!
kkkkk
'''