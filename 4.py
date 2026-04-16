'''
#4
Crea una clase llamada Libro con atributos titulo, autor y año_publicacion. 
Implementa un método que devuelva una descripción del libro y otro que verifique si el libro es 
considerado un clásico (publicado hace más de 50 años).
'''
from datetime import date

class libro:
    def __init__(self, nombre, descripcion, publicacionannio):
        self._nombre = nombre
        self._descripcion = descripcion
        self._publicacionannio = publicacionannio
    # Getters
    def GetDescrition(self):
        return self._descripcion
    
    def VerifyClassic(self):
        anio_actual = date.today().year
        diferencia = anio_actual - self._publicacionannio
        if diferencia >= 50:
            return True
        else:
            return False

if __name__ == "__main__":
    libro1 = libro("Hola libro god", "descripcionexampleinsert", 1943)
    libro2 = libro("libronuevo", "lo hice ayer  hola", 2024)
    
    esclasico = libro1.VerifyClassic()
    print("LIBRO1:")
    if esclasico:
        print("eee un classic weei")
        print(f"{libro1.GetDescrition()}")
    else:
        print("nooo es un clasico hola")
        
    esclasico2 = libro2.VerifyClassic()
    print("LIBRO2:")
    if esclasico2:
        print("eee un classic weei")
        print(f"{libro2.GetDescrition()}")
    else:
        print("nooo es un clasico")
        
    
