'''
#5
Crea una clase llamada Estudiante que tenga atributos como nombre, edad y notas (una lista de números). 
Implementa métodos para agregar una nota y calcular el promedio de las notas.
'''

class alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.Notas = []
    
    # getters
    def CalcularPromedio(self):
        cantidadnotas = len(self.Notas)
        sumatotal = 0
        for nota in self.Notas:
            sumatotal = sumatotal + nota
        return sumatotal / cantidadnotas
    
    # setters
    def AddNote(self, nota):
        try:
            numero = int(nota)
            self.Notas.append(nota)
            print("Nota ingresada")
        except ValueError:
            print("Valor no valido.")

if __name__ == "__main__":
    alumno1 = alumno("Tomas", 188)
    alumno1.AddNote(7)
    alumno1.AddNote(3)
    alumno1.AddNote(6)
    alumno1.AddNote(8)
    print(f"Promedio: {alumno1.CalcularPromedio()}")