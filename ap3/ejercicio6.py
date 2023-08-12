class Carta:
    def __init__(self, valor, pinta):
        PINTAS = ('Corazones', 'Diamantes', 'Tréboles', 'Picas') #tupla PINTAS

        self.valor = valor 
        self.pinta = pinta 

mi_carta = Carta('10', 'Picas')

# Acceder a las propiedades de la carta
print("Valor de la carta:", mi_carta.valor)
print("Pinta de la carta:", mi_carta.pinta)