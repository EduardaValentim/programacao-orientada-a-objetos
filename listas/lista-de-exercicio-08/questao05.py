class Pokemon:
    def __init__(self, nome, tipo, descricao, ataques, nivel, poder_luta, brilhante):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = []
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante = brilhante

    def mostrar_ataques(self):
        return print(self.ataques)

    def subir_nivel(self):
        self.nivel += 1
        self.poder_luta += 2
        return self.nivel and self.poder_luta

    def mostrar_poder_luta(self):
        return print(self.poder_luta)

    def e_brilhante(self):
        return print(self.brilhante is 'Sim')
        
    def adicionar_ataque(self, novo_ataque):
        self.ataques.append(novo_ataque)
        return self.ataques

    def caracteristicas(self):
        return print('NOME: {} \nNÍVEL: {}\nTIPO: {} \nDESCRIÇÃO: {} \nATAQUES: {} \nPODER DE LUTA: {} \nBRILHANTE: {}'.format(self.nome, self.nivel, self.tipo, self.descricao, self.ataques, self.poder_luta, self.brilhante is 'Sim'))


p1 = Pokemon('Pikachu', 'Elétrico', 'Condutor de energia elétrica e pode manipular energia elétrica lançando rajadas de trovões e relâmpagos', [], 1, 1, 'Sim')
p1.subir_nivel()
p1.adicionar_ataque('Trovao')
p1.caracteristicas()