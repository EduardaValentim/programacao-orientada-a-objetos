class Tamagotchi:
    def __init__(self, nome, fome=10, saude=10, idade=0):
        self.nome = nome
        self.fome = 10
        self.saude = 10
        self.idade = 0
        print(self.nome)

    def alterar_nome(self, nome):
        self.nome = nome
        return print(self.nome)

    def retornar_fome(self):
        return print(self.fome)

    def retornar_saude(self):
        return print(self.saude)

    def retornar_idade(self):
        return print(self.idade)

    def comer(self):
        self.fome += 1
        if self.fome > 10:
            self.fome = 10
            return self.fome
        return self.fome

    def tomar_injecao(self):
        self.saude += 1
        if self.saude > 10:
            self.saude = 10
            return self.saude
        return self.saude
    def envelhecer(self):
        self.idade += 1
        self.saude -= 1
        if self.saude < 0:
            self.saude = 0
            return self.idade and self.saude
        return self.idade and self.saude

t1 = Tamagotchi('Suzy')
t1.retornar_fome()
t1.retornar_saude()
t1.retornar_idade()
t1.comer()
t1.tomar_injecao()
t1.envelhecer()
t1.retornar_fome()
t1.retornar_saude()
t1.retornar_idade()