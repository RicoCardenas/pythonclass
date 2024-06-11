#de esta forma no es muy logico usarlo, es muy usado para crear listas vacias(lista = list()
lista = list(["Hola", "Mundo", "Python"])

#regresar tamaño de la lista(len())
metodo_ejecutado1 = len(lista)
print(metodo_ejecutado1)

#agregando elementos a la lista (append()), se le pasa el elemento a agregar
lista.append("Julian")
print(lista)

#agregamos elementos a la lista en una posicion especifica (insert()), se le pasa la posicion y el elemento a agregar
lista.insert(2, "Alejandro")
print(lista)

#agregando varios elementos a la lista (extend()), se le pasa una lista con los elementos a agregar
lista.extend(["Duarte", "es", "homosexual"])
print(lista)

#eliminando elemento de la lista por su indice (pop()), se le pasa el indice del elemento a eliminar
lista.pop(-1)
print(lista)
#para eliminar el ultimo elemento de la lista, se le coloca -1, o directamente sin pasarle nada, -2 para eliminar el penultimo, etc....

#eliminando elemento de la lista por su valor (remove()), se le pasa el valor del elemento a eliminar
lista.remove("Alejandro")
print(lista)

#eliminar todos los elementos de la lista (clear())
#lista.clear()
#print(lista)

#ordenar los elementos de forma ascendente, pero solo si es cadena numerica (sort())
lista_2 = [1, 5, 3, 2, 4]
lista_2.sort()
print(lista_2)
#una forma de ordenarlos de mayor a menor es usar la misma funcion pero agregarle el parametro reverse=True
lista_2.sort(reverse=True)
print(lista_2)

#invierte los elementos de una lista, a diferencia del sort, es que el reverse, no los organiza de menos a mayor, sino que directamente los revierte, en el orden actual de la lista
lista.reverse()
print(lista)

print(dir(set[1,2,3]))
#metodo para ver los metodos de una lista