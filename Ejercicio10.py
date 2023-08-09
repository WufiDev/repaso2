#Escribir una función que calcule el factorial de un número dado.

def factorial_bucle(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número: "))
factorial = factorial_bucle(numero)
print(f"El factorial de {numero} es {factorial}")

