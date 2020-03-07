'''
metodo estatico apenas devolve informação não altera nada
'''
class Humano:
    especie = 'Homo sapiens'
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo neaderthalens'

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Neaderthalenis', 'Erectus', 'Spiens')
        return ('Austrolopiteco') + tuple(f'Homo {adj}' for adj in adjetivos)

class Neaderthalenis(Humano):
    especie = Humano.especies()[-2]
    


if __name__=='__main__':

    jose = Humano('José')
    grokn = Humano('Grokn')

    print(f'Humano.especie: {Humano.especie}')
    print(f'Humano.especie: {jose.especie}')

    grokn.das_cavernas()
    print(f'Humano.especie: {grokn.especie}')
    print(f'Humano.especie: {jose.especies()}')


