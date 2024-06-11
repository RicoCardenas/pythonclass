lista = ["sinisterra", 2, "julian cardenas"]
lista.append("julian")
print(lista)
print(type(lista))
print(len(lista))
print(lista[0])
# la lista es una variable que se puede modificar y se define con corchetes


tople = ("sinisterra", 2, "julian cardenas")
print(tople)
print(type(tople))
print(len(tople))
print(tople[0])
# la tupla es una variable que no se puede modificar y se define con parentesis

sete = {"sinisterra", 2, "julian cardenas"}
sete.add("julian")
print(sete)
print(type(sete))
print(len(sete))
# el set es una variable que no se puede modificar pero se le pueden ingresar datos y se define con llaves, tampoco es posible acceder a los elementos de la misma forma que una lista o tupla: lista[0] o tupla[0]

#creando un diccionario (dict)

diccionario = {
    'nombre': "Julian Cardenas",
    'edad': 22,
    'cursos': ["Python", "Django", "JavaScript"]
}
print(diccionario['nombre'])