cadena_1 = "Hola soy Julian"
cadena_2 = "Bienvenido"
lista = ["Hola", "soy", "Julian"]

#convierte a mayusculas (upper())
metodo_ejecutado1 = cadena_1.upper()
print(metodo_ejecutado1)

#convierte a minusculas (lower())
metodo_ejecutado2 = cadena_1.lower()
print(metodo_ejecutado2)

#convierte primera letra en mayuscula (capitalize())
metodo_ejecutado3 = cadena_1.capitalize()
print(metodo_ejecutado3)

#buscamos una cadena en otra cadena (find()), si no encuentra retorna -1, retorna la posicion en la que se encuentra, (en una lista siempre comienza a contar desde 0)
metodo_ejecutado4 = cadena_1.find("Julian")  
print(metodo_ejecutado4)

#funciona igual que find(), pero si no encuentra una coincidencia, no arroja -1, arroja un error (index())
metodo_ejecutado5 = cadena_1.index("Julian")
#metodo_ejecutado5 = cadena_1.index("julian"), arroja error
print(metodo_ejecutado5)

#si es numerico devuelve true, si no false (isnumeric())
metodo_ejecutado6 = cadena_1.isnumeric()
print(metodo_ejecutado6)

#si es alfanumerico devuelve true, si no false (isalpha()), los espacios no son valores alfanumericos
metodo_ejecutado7 = cadena_1.isalpha()
print(metodo_ejecutado7)

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coinciden (count()), si no encuentra retorna 0
metodo_ejecutado8 = cadena_1.count("a")
print(metodo_ejecutado8)

#devuelve la longitud de la cadena (len()), len es una funcion, no un metodo, no se escribe conp punto, se escribe directamente len(cadena)
metodo_ejecutado9 = len(cadena_1)
print(metodo_ejecutado9)

#verificado si una cadena comienza con otra cadena dada (startswith()), devuelve true o false
metodo_ejecutado10 = cadena_1.startswith("Hola") #devuelve true
#metodo_ejecutado10 = cadena_1.startswith("hola") devuelve false
print(metodo_ejecutado10)

#verificado si una cadena termina con otra cadena dada (endswith()), devuelve true o false
metodo_ejecutado11 = cadena_1.endswith("Julian") #devuelve true
#metodo_ejecutado11 = cadena_1.endswith("julian") devuelve false
print(metodo_ejecutado11)

#reemplaza una cadena por otra (replace()), se le pasa la cadena a reemplazar y la cadena que reemplazara, en caso de encontrar similitud
#es muy usado para quitar espacios en blanco, o reemplazar caracteres
metodo_ejecutado12 = cadena_1.replace("Julian", "Alejandro")
print("\nReemplaza Julian por Alejandro en la cadena:")
print(cadena_1)
print(metodo_ejecutado12)

#separar una cadena en una lista (split()), se le pasa el caracter por el cual se separara la cadena, si no se le pasa nada, separa por espacios
metodo_ejecutado13 = cadena_1.split()
print("\n", metodo_ejecutado13)
#metodo_ejecutado13 = cadena_1.split(".") #separara la cadena cada que se encuentra un punto

#unir una lista en una cadena (join()), se le pasa la lista a unir, es una funcion no es un metodo, no se escribe con punto, se escribe directamente join(lista)
metodo_ejecutado14 = " ".join(lista)
print("\n", metodo_ejecutado14)