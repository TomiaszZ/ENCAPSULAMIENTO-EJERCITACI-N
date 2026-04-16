'''
# Problema 1
    Crea una clase llamada Auto que tenga los siguientes atributos: marca, modelo y año. 
    Implementa un método que muestre la información del coche en un formato legible.
    
'''


class auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        return f"auto: {self.marca} {self.modelo}, Año: {self.año}"

# Ejemplo de uso
if __name__ == "__main__":
    auto1 = auto("Toyota", "Corolla", 2020)
    print(auto1.mostrar_informacion())
