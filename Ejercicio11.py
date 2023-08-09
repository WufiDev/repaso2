#Crear un programa que genere una lista de números pares entre 1 y 100.

lista_pares = []

for numero in range(1,101):
    if (numero %2 == 0) :
        lista_pares.append(numero)
    
print("La lista generada es: ", lista_pares )