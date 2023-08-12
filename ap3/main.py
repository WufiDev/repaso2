from cuenta_bancaria import CuentaBancaria

# Crear una instancia de la clase CuentaBancaria
cuenta1 = CuentaBancaria("123456789", ["Juan", "María"], 1000)

# Realizar operaciones en la cuenta
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.aplicar_cuota_manejo()

# Mostrar detalles de la cuenta
cuenta1.mostrar_detalles()