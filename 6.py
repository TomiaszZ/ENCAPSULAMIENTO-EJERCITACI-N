'''
#6
Crea una clase llamada Rectángulo que tenga atributos base y altura. 
Implementa métodos para calcular el área y el perímetro del rectángulo.
'''

class Rectangulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
    
    def CalcularArea(self):
        return self.altura * self.anchura
        
    def CalcularPerimetro(self):
        return 2 * (self.altura + self.anchura)

if __name__ == "__main__":

    mi_rectangulo = Rectangulo(10, 5)
    
    print(f"altura: {mi_rectangulo.altura}")
    print(f"Anchura: {mi_rectangulo.anchura}")
    
    area = mi_rectangulo.CalcularArea()
    print(f"area calculada: {area}")
    
    perimetro = mi_rectangulo.CalcularPerimetro()
    print(f"perimetro calculado: {perimetro}")