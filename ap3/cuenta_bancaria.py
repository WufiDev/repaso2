class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        
    def depositar(self, monto):
        self.balance += monto
        
    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else:
            print("Fondos insuficientes")
            
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        
    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)