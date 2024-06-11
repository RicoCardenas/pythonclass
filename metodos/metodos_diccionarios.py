diccionario_1 = {
    'nombre': "Julian",
    'apellido': "Cardenas",
    'edad': 22,
}

#imprime las claves-keys del diccionario
claves = diccionario_1.keys()
print(claves)

#devuelve el valor de alguna clave get('nombre_de_clave'), si no encuentra coincidencia, en vez de lanzar un error me arroja un none
valor_clave1 = diccionario_1.get('nombre')   
print(valor_clave1)

#eliminando todos los elementos del diccionario (clear())
#diccionario_1.clear()
#print(diccionario_1)

#elimnar un elemento del diccionario pop('nombre_de_clave')
diccionario_1.pop('nombre')
print(diccionario_1)

