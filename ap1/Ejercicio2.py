#Escribir una función que calcule el área de un círculo dado su radio.

def calcular_area_circulo(radio):
    pi_aproximado = 3.14159
    area = pi_aproximado * radio ** 2
    return area

radio_usuario = float(input("Ingresa el radio del círculo: "))

area_resultante = calcular_area_circulo(radio_usuario)
print("El área del círculo con radio", radio_usuario, "es:", area_resultante)