'''
#7
Crea una clase llamada Empleado con atributos nombre, salario y departamento. 
Implementa un metodo que aumente el salario en un porcentaje dado y otro que muestre la informacion del empleado.
'''

class empleado:
    def __init__(self, nombre, salario, departamento):
        self._nombre = nombre
        self._salario = salario
        self._departamento = departamento
    
    # getters
    def getNombre(self):
        return self._nombre
    def getSalario(self):
        return self._salario
    def getDepartamento(self):
        return self._departamento
    
    def mostrarInfo(self):
        return f"Empleado: {self.getNombre()} | Departamento: {self.getDepartamento()} | Salario: ${self.getSalario():.2f}"
    
    # setters
    def aumentarSalario(self, porcentaje):
        try:
            factor = float(porcentaje) / 100
            print(f"SALARIO ANTERIOR: {self._salario}")
            self._salario = self._salario + (self._salario * factor)
            print(f"SALARIO CON AUMENTO: {self._salario}")
        except ValueError:
            print(f"Porcentaje no valido.")

if __name__ == "__main__":

    emp1 = empleado("Carlos Gomez", 2500, "Ventas")
    print(emp1.mostrarInfo())
    emp1.aumentarSalario(160) 
    print(emp1.mostrarInfo())

    emp2 = empleado("Ana Ruiz", 3000, "Sistemas")
    print(emp2.mostrarInfo())
    emp2.aumentarSalario(15)
    print(f"Nuevo salario de {emp2.getNombre()}: ${emp2.getSalario()}")
