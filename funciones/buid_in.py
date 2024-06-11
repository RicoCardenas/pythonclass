numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#encontrando el numero mayor de una lista

numero_mas_alto = max(numeros)
print(numero_mas_alto)
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando un numero

numero = 3.1416
redondear_numero = round(numero,3)
print(redondear_numero)

#Retorna False si el valor es 0, None, False o una cadena vacia y retorna True en cualquier otro caso
resultado_bool = bool(True)
print(resultado_bool)

#Funcion all retorna true, si todos los valores son verdaderos
resultado_all = all(numeros)
print(resultado_all)

#suma todos los valores de un iterable
resultado_sum = sum(numeros)
print(resultado_sum)