class Computador:
    def __init__(self, marca, modelo, componentes, anos_uso, cor):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor
        #print(self.marca, self.modelo, self.componentes, self.anos_uso, self.cor)
    
    def mostrarMarca(self):
        return print(self.marca)
    
    def adicionarComponentes(self, componente):
        self.componentes.append(componente)
        return self.componentes
    
    def mostrarComponentes(self):
        return print(self.componentes)

    def mostrar_anos_uso(self):
        if self.anos_uso < 6:
            return print(self.anos_uso)
        else:
            return print('Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora...')
    
    def envelhecer(self):
        self.anos_uso += 1
        return self.anos_uso

c1 = Computador('positivo', 'modelo1', ['monitor', 'teclado', 'mouse'], 2, 'azul')
c1.mostrarMarca()
c1.mostrarComponentes()
c1.adicionarComponentes('luzes')
c1.mostrarComponentes()
c1.mostrar_anos_uso()
c1.envelhecer()
c1.mostrar_anos_uso()