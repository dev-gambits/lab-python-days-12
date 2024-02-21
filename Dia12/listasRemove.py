"""
Definición de una lista de números
Recorrido e impresión de los elementos de la lista
Agregar un elemento a la lista
Eliminar un elemento de la lista
"""
numeros = [1, 2, 3, 4, 5]
print("Elementos de la lista:")
for numero in numeros:
    print(numero)

numeros.append(6)
print("Lista después de agregar un elemento:", numeros)

numeros.remove(3)
print("Lista después de eliminar el elemento 3:", numeros)
