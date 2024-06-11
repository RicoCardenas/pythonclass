animales = ["perro", "gato", "loro", "pez", "serpiente"]

#animal sera una variable que se creara solo dentro del bucle for
for animal in animales:
    #recorriendo lista animales
    print(f"ahora la variable animal es igual a: {animal}")
    
#recorriendo string, tupla y diccionario
name = "Julian"

for nombre in name:
    #recorriendo string name
    print(nombre)
    
tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    #recorriendo tupla
    print(numero)
    
for tuple,i in enumerate(tupla):
    #recorriendo tupla con su indice
    print(f"indice: {tuple} valor: {i}")
 
diccionario = {"nombre": "Julian", "edad": 25, "ciudad": "Bogota"}

for key in diccionario.items():
    #recorriendo diccionario
    print(key)
    
#Iterar dos listas a la vez

#CONDICIONES: las 2 listas deben tener la misma cantidad de elementos, de lo contrario se generara un error

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["uno", "dos", "tres", "cuatro", "cinco"]

for lista1,lista2 in zip(lista_1, lista_2):
    #recorriendo 2 listas a la vez
    print(f"{lista1}:{lista2}")
    
    
#iterar con funcion range
for num in range(5,10):
    #recorriendo rango de 5 a 9
    print(num)
    
#forma correcta de recorrer una lista con su indice
for i in enumerate(animales):
    #recorriendo lista con su indice
    print(i)
    
    
#usando for/else
for number in tupla :
    #recorriendo tupla
    print(number)
else:
    print("fin del bucle")
    


