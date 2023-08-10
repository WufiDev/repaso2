#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

def es_palindromo(cadena):
    cadena = cadena.lower() 
    cadena = cadena.replace(" ", "") 
    return cadena == cadena[::-1]  

cadena_usuario = input("Ingresa una cadena de texto: ")

if es_palindromo(cadena_usuario):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
