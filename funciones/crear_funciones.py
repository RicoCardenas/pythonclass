import random
def primera_funcion():
    print("Hola, soy la primera función")
    
primera_funcion()

for primera in range(1,5):
    primera_funcion()
    
#crear funcion con parametros

def funcion_parametro(nombre, sexo):
    nombre = nombre.capitalize()
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "hermosa"
    elif(sexo == "hombre"):
        adjetivo = "caballerosa"
    else:
        adjetivo = "estimado"
        
    print(f"Hola {nombre}, mi {adjetivo} amistad")
    
    
funcion_parametro("julian", "hombre")

#funcion que retorne valores
def crear_contraseña(contra):
    listado_de_caracteres = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "!@#$%^&*()"]
    contrasena = ""
    for i in range(0, contra):
        cadena = random.choice(listado_de_caracteres) #elige una cadena aleatoria
        caracter = random.choice(cadena) #elige un caracter aleatorio de la cadena
        contrasena += caracter
    print(contrasena)

crear_contraseña(10)

#otra forma de crear contraseña

def otro_forma(num):
    chars = "abcdefghijklmnñopqrstuvwxyz"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    print(contraseña)
    
otro_forma(15)