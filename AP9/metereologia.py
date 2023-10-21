from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_total = 0
        direccion_viento = {}

        with open(self.nombre_archivo, 'r') as archivo:
            num_estaciones = 0

            for linea in archivo:
                partes = linea.strip().split(': ')
                if len(partes) == 2:
                    clave, valor = partes

                    if clave == 'Temperatura':
                        temperatura_total += float(valor)
                    elif clave == 'Humedad':
                        humedad_total += float(valor)
                    elif clave == 'Presion':
                        presion_total += float(valor)
                    elif clave == 'Viento':
                        velocidad, direccion = valor.split(',')
                        velocidad_total += float(velocidad)
                        if direccion in direccion_viento:
                            direccion_viento[direccion] += 1
                        else:
                            direccion_viento[direccion] = 1

                    if clave == 'Estacion':
                        num_estaciones += 1

        # Promedio
        temperatura_promedio = temperatura_total / num_estaciones
        humedad_promedio = humedad_total / num_estaciones
        presion_promedio = presion_total / num_estaciones
        velocidad_promedio = velocidad_total / num_estaciones

        # dirección predominante del viento
        direccion_grados = {
            'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5,
            'E': 90, 'ESE': 112.5, 'SE': 135, 'SSE': 157.5,
            'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5,
            'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
        }
        grados_total = 0
        for direccion, cantidad in direccion_viento.items():
            grados_total += direccion_grados[direccion] * cantidad
        direccion_promedio_grados = grados_total / num_estaciones

        for direccion, grados in direccion_grados.items():
            if abs(direccion_promedio_grados - grados) < 11.25:
                direccion_predominante = direccion
                break
        else:
            direccion_predominante = 'N'

        return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio, direccion_predominante)

archivo_datos = 'datos_climaticos.txt'
datos = DatosMeteorologicos(archivo_datos)
estadisticas = datos.procesar_datos()
print(f"Temperatura promedio: {estadisticas[0]}°C")
print(f"Humedad promedio: {estadisticas[1]}%")
print(f"Presion promedio: {estadisticas[2]} hPa")
print(f"Velocidad promedio del viento: {estadisticas[3]} km/h")
print(f"Dirección predominante del viento: {estadisticas[4]}")
