'''
# Problema 2
    Crea una clase llamada Persona con atributos nombre, edad y sexo. 
    Implementa un método que permita cambiar la edad de la persona y otro que muestre la información de la persona.
    
'''

class persona:
    def __init__(self, edad, nombre, apellido, sexo):
        self._edad = edad
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo

    # Getters
    def Obtener_nombre(self):
        return self._nombre
    def obtener_apellido(self):
        return self._apellido
    def obtener_edad(self):
        return self._edad
    def obtenersexo(self):
        return self._sexo
    
    # Setters
    def EstablecerEdad(self, edadInput):
        self._edad = edadInput

# Ejemplo de uso
if __name__ == "__main__":
    usuario = persona(25, "Geronimo", "Benavidez", "Masculino")

    print(f"Nombre: {usuario.Obtener_nombre()} {usuario.obtener_apellido()}")
    print(f"Edad inicial: {usuario.obtener_edad()}")
    print(f"genero: {usuario.obtenersexo()}")

    usuario.EstablecerEdad(26)
    print(f"Feliz cumple momo {usuario.Obtener_nombre()}: {usuario.obtener_edad()}")
