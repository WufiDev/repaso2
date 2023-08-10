#Crear un programa que genere una matriz de números y la imprima en pantalla.

filas = 3
columnas = 4

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = i * columnas + j + 1  
        fila.append(numero)
    matriz.append(fila)

for fila in matriz:
    print(fila)
