from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

def __eq__(self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

class Conjunto():
    contador = 0
    
    def __init__(self, nombre):
     Conjunto.contador +=1 
     self.elementos = []
     self.nombre = str = nombre 
     self.__id = Conjunto.contador  # Asignar el valor del contador a __id

    @property
    def id(self):
        return self.__id  # Propiedad de solo lectura para acceder a __id
    
    def contiene(self, elemento):
        if isinstance(elemento, Elemento):
            for elem in self.elementos:
                if elem == elemento:
                    return True
        return False
    
    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(self.nombre + " UNIDO " + otro_conjunto.nombre)
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto
    
    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [e for e in conjunto1.elementos if conjunto2.contiene(e)]
        nombre_conjunto_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_conjunto_interseccion)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto
    
    def __str__(self):
        elementos_str = ", ".join(str(e.nombre) for e in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
    
elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")
elemento4 = Elemento("B")

conjunto1 = Conjunto("Conjunto A")
conjunto2 = Conjunto("Conjunto B")

conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto1.agregar_elemento(elemento3)

conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento4)

print(conjunto1)
print(conjunto2)

union = conjunto1 + conjunto2
print(union)

interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)