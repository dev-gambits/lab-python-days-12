"""
Definición de un diccionario de estudiantes
Acceso e impresión de los datos del diccionario
Agregar un nuevo estudiante al diccionario
Eliminar un estudiante del diccionario
"""

estudiantes = {
    "Juan": 18,
    "María": 20,
    "Carlos": 19
}

print("Edad de Juan:", estudiantes["Juan"])
print("Edad de María:", estudiantes.get("María"))

estudiantes["Ana"] = 21
print("Diccionario después de agregar a Ana:", estudiantes)

del estudiantes["Carlos"]
print("Diccionario después de eliminar a Carlos:", estudiantes)
