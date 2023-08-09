#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

numeros = [12,34,56,78,90]

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("El número más grande en la lista es:", mayor)
print("El número más pequeño en la lista es:", menor)