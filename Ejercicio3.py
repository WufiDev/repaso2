#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random

cantidad_numeros = 10  

numeros_aleatorios = []  

for _ in range(cantidad_numeros):
    numero_aleatorio = random.randint(1, 100) 
    numeros_aleatorios.append(numero_aleatorio)  

print("Lista de números aleatorios:", numeros_aleatorios)