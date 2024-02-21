"""
Definición de una clase
Creación de un objeto de la clase Persona
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 30)
persona2 = Persona("Antonio", 35)
persona3 = Persona("Lucas", 3)

# Llamada al método de la clase
persona1.saludar()  # Output: Hola, me llamo Ana y tengo 30 años.
persona2.saludar()
persona3.saludar()