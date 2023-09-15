from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.elementos = []

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elemento == e for e in self.elementos)

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
    


    