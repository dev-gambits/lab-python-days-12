"""
Importamos el módulo os, que proporciona funciones para interactuar con el sistema operativo.
Definimos una función llamada borrar_archivo que intentará eliminar un archivo en la ruta especificada.
Intentamos eliminar el archivo especificado por la ruta utilizando la función os.remove().
En caso de que ocurra una excepción durante la eliminación del archivo, capturamos el error y lo imprimimos.
Llamamos a la función borrar_archivo con la ruta del archivo que queremos eliminar como argumento.
"""
import os

def borrar_archivo(ruta_archivo):
    try:
        os.remove(ruta_archivo)
    except Exception as e:
        print(e)
borrar_archivo("archivos_ejemplo/archivo_borrar.txt")
