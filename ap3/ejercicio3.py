import math 

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

# Crear instancias de la clase Punto
punto1 = Punto(3, 5)
punto2 = Punto(7, 9)

# Mostrar las coordenadas del punto1
punto1.mostrar()

# Mover el punto2 a nuevas coordenadas
punto2.mover(10, 12)
punto2.mostrar()

# Calcular la distancia entre punto1 y punto2
distancia = punto1.calcular_distancia(punto2)
print("Distancia entre punto1 y punto2:", distancia)