igual_que = 5 == 4
print(igual_que)

distinto_de = 5 != 4
print(distinto_de)

mayor_que = 5 > 4
print(mayor_que)

menor_que = 5 < 4
print(menor_que)

menor_igual = 5 <= 4
print(menor_igual)  

mayor_igual = 5 >= 4
print(mayor_igual)

#comparar usuarios
usuario_base_datos = "julian cardenas"

usuario_escrito = input("Ingrese su usuario: ")

if usuario_base_datos == usuario_escrito.lower():
    print("Usuario correcto")
else:
    print("Usuario incorrecto")