#6
# Crea una clase llamada Rectangulo que tenga atributos base y altura. 
# Implementa metodos para calcular el area y el perimetro del rectangulo.

class Rectangulo:
    def __init__(self, altura, anchura):
        self._altura = altura
        self._anchura = anchura
    
    # Getters
    def getAltura(self):
        return self._altura
    
    def getAnchura(self):
        return self._anchura
    
    def CalcularArea(self):
        return self._altura * self._anchura
        
    def CalcularPerimetro(self):
        return 2 * (self._altura + self._anchura)

if __name__ == "__main__":

    mi_rectangulo = Rectangulo(10, 5)
    
    print(f"altura: {mi_rectangulo.getAltura()}")
    print(f"Anchura: {mi_rectangulo.getAnchura()}")
    
    area = mi_rectangulo.CalcularArea()
    print(f"area calculada: {area}")
    
    perimetro = mi_rectangulo.CalcularPerimetro()
    print(f"perimetro calculado: {perimetro}")
