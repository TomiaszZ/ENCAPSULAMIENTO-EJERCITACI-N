'''
#9
Crea una clase llamada Juego que tenga atributos nombre, género y precio. 
Implementa un método que muestre la información del juego y otro que verifique 
si el juego está en oferta (si el precio es menor a un valor dado).
'''
class juego():
    def __init__(self, nombre, precio, genero):
        self.nombre = nombre
        self.precio = precio
        self.genero = genero
    # getters
    def getNombre(self):
        return self.nombre
    def getPrecio(self):
        return self.precio
    def getGenero(self):
        return self.genero
    
    def Verifoferta(self, valorin):
        try:
            valor = int(valorin)
        except ValueError:
            print("Introduce un valor valido")

if __name__ == "__main__":