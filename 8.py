#8
# Crea una clase llamada Producto que tenga atributos nombre, precio y stock. 
# Implementa metodos para aumentar y disminuir el stock, asegurandote de que no se pueda tener un stock negativo.

class producto:
    def __init__(self, Nombre, precio):
        self._nombre = Nombre
        self._precio = precio
        self._stock = 0
    
    def getNombre(self):
        return self._nombre

    def getPrecio(self):
        return self._precio

    def getStock(self):
        return self._stock
    
    def AddStock(self, units):
        try:
            unidades = int(units)
            self._stock += unidades
            print(f"cantidad de stock de {self._nombre}: {self._stock}")
        except ValueError:
            print("Introduce un valor valido")
            
    def RemoveStock(self, units):
        try:
            unidades = int(units)
            if unidades > self._stock:
                print(f"No puedes retirar {unidades} unidades. Solo hay {self._stock} en stock.")
            else:
                self._stock -= unidades
                print(f"cantidad de stock de {self._nombre}: {self._stock}")
        except ValueError:
            print("Introduce un valor valido")

if __name__ == "__main__":
    prod1 = producto("Monitor Gamer", 300)
    print(f"Producto: {prod1.getNombre()} | Precio: ${prod1.getPrecio()}")
    
    prod1.AddStock(50)      
    prod1.RemoveStock(20)  
    prod1.RemoveStock(40)

    prod2 = producto("Teclado Mecanico", 85)
    print(f"Producto: {prod2.getNombre()} | Stock Inicial: {prod2.getStock()}")

    prod2.AddStock(10)
    prod2.RemoveStock("hola") 
    print(f"Stock final de {prod2.getNombre()}: {prod2.getStock()}")
