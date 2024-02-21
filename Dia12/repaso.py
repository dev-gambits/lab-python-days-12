"""
Intentar modificar el primer elemento del conjunto es inválido y generará un error.
Por lo tanto, la línea a continuación está comentada para evitar un error de asignación.
equipaje[0] = "abrigo"
Accedemos al primer elemento del conjunto usando el índice 0 y lo imprimimos.
"""

equipaje = ("camisa", "pantalón", "vestido", "calcetines", "zapatos", "mocacines", "corbata")
mensaje = 'El índice es: '
print(mensaje, equipaje[0])
print(mensaje, equipaje[1])
print(mensaje, equipaje[2])
print(mensaje, equipaje[3])
print(mensaje, equipaje[4])
# print(mensaje, equipaje[0])
print(mensaje, equipaje[5])
print(mensaje, equipaje[6])