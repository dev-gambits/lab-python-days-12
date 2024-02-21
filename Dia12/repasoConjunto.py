"""
Creamos un conjunto llamado "invitados" con nombres de personas.
Imprimimos el conjunto de invitados.
No podemos acceder a elementos individuales de un conjunto por índice,
ya que los conjuntos son colecciones desordenadas y no admiten indexación.
Iteramos sobre cada elemento en el conjunto "invitados" e imprimimos el nombre de cada invitado.
"""
invitados = {"Luis", "Ana", "Sebastián", "Sofía", "Mateo", "Ana", "Sebastián", 'Emmanuel', "Mateo"}

print("Lista de invitados:", invitados)

for invitado in invitados:
    print(f"Nombre de invitado(a): {invitado}")


# Recordar qe los conjuntos no permiten datos duplicados, los omite
