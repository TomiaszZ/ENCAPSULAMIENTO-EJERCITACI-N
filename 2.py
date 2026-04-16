'''
# Problema 2
    Crea una clase llamada Persona con atributos nombre, edad y sexo. 
    Implementa un método que permita cambiar la edad de la persona y otro que muestre la información de la persona.
    
'''

class persona:
    def __init__(self, edad, nombre, apellido):
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido

    # Getters
    def Obtener_nombre(self):
        return self.nombre
    def obtener_apellido(self):
        return self.apellido
    def obtener_edad(self):
        return self.edad
    
    # Setters
    def EstablecerEdad(self, edadInput):
        self.edad = edadInput

# Ejemplo de uso
if __name__ == "__main__":
    usuario = persona(25, "Geronimo", "Benavidez")

    print(f"Nombre: {usuario.Obtener_nombre()} {usuario.obtener_apellido()}")
    print(f"Edad inicial: {usuario.obtener_edad()}")

    usuario.EstablecerEdad(26)
    print(f"Feliz cumple momo {usuario.Obtener_nombre()}: {usuario.obtener_edad()}")