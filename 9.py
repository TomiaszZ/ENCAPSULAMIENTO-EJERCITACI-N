'''
#9
Crea una clase llamada Juego que tenga atributos nombre, género y precio. 
Implementa un método que muestre la información del juego y otro que verifique 
si el juego está en oferta (si el precio es menor a un valor dado).
'''
class juego():
    def __init__(self, nombre, precio, genero):
        self._nombre = nombre
        self._precio = precio
        self._genero = genero
    # getters
    def getNombre(self):
        return self._nombre
    def getPrecio(self):
        return self._precio
    def getGenero(self):
        return self._genero
    
    def mostrarinfo(self):
        print(f" {self.getGenero()} , ${ self.getPrecio()}, {self.getGenero()}")
    
    def Verifoferta(self, valorin):
        try:
            valor_limite = float(valorin)
            if self._precio < valor_limite:
                return True
            else:
                return False
        except ValueError:
            print("Introduce un valor valido")
            return False

if __name__ == "__main__":
    juego1 = juego("Cyberpunk 2077", 30, "RPG")
    juego1.mostrarinfo()
    limite = 40
    if juego1.Verifoferta(limite):
        print(f"Oferta El precio es menor a ${limite}")
    else:
        print(f"No esta en oferta (Supera los ${limite})")

    juego2 = juego("Elden Ring", 60, "Souls-like")
    juego2.mostrarinfo()
    if juego2.Verifoferta(40):
        print("Oferta detectada")
    else:
        print("Precio normal zzZzZzZzZzZZz")
