'''
#3
Crea una clase llamada CuentaBancaria que tenga atributos como titular, saldo y numero_cuenta. 
Implementa metodos para depositar y retirar dinero, asegurandote de que el saldo no se vuelva negativo.

'''
class cuentabancaria:
    def __init__(self, saldo, titular, numerocuenta):
        self.saldo = saldo
        self.titular = titular
        self.numerocuenta = numerocuenta
    
    # Getters
    def obtenertitular(self):
        return self.titular
    def obtenercuenta(self):
        return self.numerocuenta
    def obtenersaldo(self):
        return self.saldo
    
    # Metodos de accion
    def depositar(self, cantidad):
        try:
            numero = int(cantidad)
            self.saldo += numero
            print(f"Saldo sumado: {numero}. Total actual: {self.saldo}")
        except ValueError:
            print("Error: La cantidad debe ser un numero entero.")
            
    def retirar(self, cantidad): 
        try:
            numero = int(cantidad)
            if numero > self.saldo:
                print(f"Error: No tienes suficiente saldo. Saldo actual: ${self.saldo}")
            else:
                self.saldo -= numero
                print(f"Retiro exitoso de ${numero}. Nuevo saldo: ${self.saldo}")
        except ValueError:
            print("Error: La cantidad debe ser un numero entero.")

if __name__ == "__main__":
    cuentabancaria1 = cuentabancaria(67, "tomy", 66666666)
    
    print(f"Info de la cuenta: {cuentabancaria1.obtenertitular()}, N#{cuentabancaria1.obtenercuenta()}, Saldo: ${cuentabancaria1.obtenersaldo()}")
    print("Seleccione una opcion (1 o 2): ")
    print("1 = Ingresar Saldo | 2 = Retirar Dinero")
    
    Opcion = input()
    
    if Opcion == "1":
        print("Ingresa la cantidad que deseas ingresar:")
        cantidadinput = input()
        cuentabancaria1.depositar(cantidadinput)
        
    elif Opcion == "2":
        print("Ingresa la cantidad que deseas retirar:")
        cantidadinput = input()
        cuentabancaria1.retirar(cantidadinput)
    else:
        print("Opcion no valida.")