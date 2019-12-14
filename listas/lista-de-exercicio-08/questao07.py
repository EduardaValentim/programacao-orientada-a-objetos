class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso     #kg
        self.altura = altura #centimetros

    def envelhecer(self):
        self.idade += 1
        return print(self.idade)

    def engordar(self, aumento):    #kg
        self.peso += aumento
        return print(self.peso)

    def emagrecer(self, perda):     #kg
        self.peso -= perda
        return print(self.peso)

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5     #centimetros
            return print(self.altura)
        else:
            return print(self.altura)

p1 = Pessoa('Carlos', 19, 70.8, 180)
p1.envelhecer()
p1.engordar(0.6)
p1.emagrecer(1.5)
p1.crescer()