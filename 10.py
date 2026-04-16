'''
#10
Crea una clase llamada Circulo que tenga un atributo radio. 
Implementa métodos para calcular el área y la circunferencia del círculo, y 
asegúrate de que el radio no pueda ser negativo.
'''

import math

class circulo:
    def __init__(self, radio):
        if radio < 0:
            print("Error: El radio no puede ser negativo. Se establecera en 0.")
            self._radio = 0
        else:
            self._radio = radio
    
    def getRadio(self):
        return self._radio
        
    def calcularArea(self):
        area = math.pi * (self._radio ** 2)
        return area
    
    def calcularCircunferencia(self):
        circunferencia = 2 * math.pi * self._radio
        return circunferencia

if __name__ == "__main__":
    mi_circulo = circulo(5)
    print(f"Radio del circulo: {mi_circulo.getRadio()}")
    print(f"Area: {mi_circulo.calcularArea():.2f}")
    print(f"Circunferencia: {mi_circulo.calcularCircunferencia():.2f}")

    circulo_error = circulo(-3)
    print(f"Radio corregido: {circulo_error.getRadio()}")
    print(f"Area con radio {circulo_error.getRadio()}: {circulo_error.calcularArea()}")
