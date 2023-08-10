#Crear una función que invierta el orden de los elementos en una lista dada.

def invertir_lista(lista):
    lista_invertida = []  
    
    for elemento in reversed(lista):  
        lista_invertida.append(elemento)  
    
    return lista_invertida  

mi_lista = [1, 2, 3, 4, 5]

lista_invertida = invertir_lista(mi_lista)

print("Lista original:", mi_lista)
print("Lista invertida:", lista_invertida)
