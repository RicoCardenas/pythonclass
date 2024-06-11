import random

#La cpu almacena un numero aleatorio entre 1 y 100
cpu_num = random.randint(1,100)
#Preguntamos el nombre al usuario y lo almacenamos en la variable name_user
name_user = input("Como te llamas?: ").capitalize()

#Saludamos al usuario y le decimos que adivine el numero secreto
print(f"Hola {name_user} he pensado un numero entre 1 y 100, tendras 8 intentos para adivinarlo")

#Se le pide al usuario que introduzca un numero, el cual se almacena en la variable user_name, que se convierte a entero con la funcion int, se hace un bucle for la cual se repetira como maximo 8 veces o hasta que el usuario adivine el numero correcto
for i in range(0,8):
    user_num = int(input("\nintroduce un numero: "))
    if user_num == cpu_num: 
        print(f"Felicidades {name_user}, si era el {cpu_num} lo haz adivinado en {i+1} intentos")
        break
    elif user_num < 1 or user_num > 100:
        print("el numero no esta permitido, perdiste un intento")
    elif user_num < cpu_num:
        print("haz elegido un numero menor al secreto")
    else:
        print("haz elegido un numero mayor al secreto")
    i += 1
    print(f"te quedan {8-i} intentos")
    if i == 8:
        print(f"\nNooo {name_user}, haz perdido, el numero secreto era, {cpu_num}, intenta de nuevo")
