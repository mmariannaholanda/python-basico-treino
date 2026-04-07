# aprendendo classes primeiro 

class Casa:
    def __init__(self, cor, quartos):
        self.cor = cor
        self.quartos = quartos

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')

casa1 = Casa('Azul', 4)
casa2 = Casa('Amarela', 6)

print('\nCasa 1:')
casa1.mostrar_cor()
print('\nCasa 2:')
casa2.mostrar_cor()
