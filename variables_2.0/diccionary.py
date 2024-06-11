# creando diccionarios
#de esta forma se pueden crear diccionarios vacios
diccionario = dict(nombre="Julian", apellido="Cardenas", edad=22)
print(diccionario)

#las listas no pueden ser claves y usamos frozenset para meter conjunto
diccionario_2 = {frozenset(["Alejandro", "Santiago"]):8}
print(diccionario_2)

#creando diccionarios con fromkeys(), si no lo cerramos con corchetes va a tomar el primer valor como un iterable
diccionario_3 = dict.fromkeys(["nombre", "apellido", "edad"])
print(diccionario_3)

#las tuplas pueden ser clave en un diccionario
diccionario_4 = {("julian", "cardenas"):8,
                 ("alejandro", "santiago"):22}