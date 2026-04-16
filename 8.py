'''
#8
Crea una clase llamada Producto que tenga atributos nombre, precio y stock. 
Implementa metodos para aumentar y disminuir el stock, asegurandote de que no se pueda tener un stock negativo.
'''
class producto:
    def __init__(self, Nombre, precio):
        self.nombre = Nombre
        self.precio = precio
        self.stock = 0
    
    # Setters
    def AddStock(self, units):
        try:
            unidades = int(units)
            self.stock += unidades
            print(f"cantidad de stock de {self.nombre}: {self.stock}")
        except ValueError:
            print("Introduce un valor valido")
            
    def RemoveStock(self, units):
        try:
            unidades = int(units)
            if unidades > self.stock:
                print(f"No puedes retirar {unidades} unidades. Solo hay {self.stock} en stock.")
            else:
                self.stock -= unidades
                print(f"cantidad de stock de {self.nombre}: {self.stock}")
        except ValueError:
            print("Introduce un valor valido")

if __name__ == "__main__":
    prod1 = producto("Monitor Gamer", 300)
    print(f"Producto: {prod1.nombre} | Precio: ${prod1.precio}")
    
    prod1.AddStock(50)      
    prod1.RemoveStock(20)  
    prod1.RemoveStock(40)
    prod2 = producto("Teclado Mecanico", 85)
    print(f"Producto: {prod2.nombre} | Stock Inicial: {prod2.stock}")

    prod2.AddStock(10)
    prod2.RemoveStock("hola")
    print(f"Stock final de {prod2.nombre}: {prod2.stock}")