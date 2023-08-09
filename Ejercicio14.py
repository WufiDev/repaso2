#Escribir una función que calcule la media aritmética de una lista de números.

def calcular_media(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media

numeros = [15, 25, 30, 40, 50]

media_calculada = calcular_media(numeros)

print("La media aritmética de la lista es:", media_calculada)