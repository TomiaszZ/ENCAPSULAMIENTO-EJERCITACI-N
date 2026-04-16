# Problema 1
    # Crea una clase llamada Auto que tenga los siguientes atributos: marca, modelo y año. 
    # Implementa un método que muestre la información del coche en un formato legible.

class auto:
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    # Getters
    def get_marca(self):
        return self._marca
    
    def get_modelo(self):
        return self._modelo
    
    def get_annio(self):
        return self._año


    def mostrar_informacion(self):
        return f"auto: {self.get_marca()} {self.get_modelo()}, año: {self.get_annio()}"

if __name__ == "__main__":
    auto1 = auto("supra", "6767", 2020)
    print(f"arca: {auto1.get_marca()}")
    print(f"modeloo: {auto1.get_modelo()}")
    print(f"año de fabricacion: {auto1.get_annio()}")
    print(auto1.mostrar_informacion())
