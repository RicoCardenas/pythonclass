import random
print("Juguemos Piedra, Papel o Tijera, Escoge: ")
print("1.Piedra, 2.Papel, 3.Tijera")
usuario = int(input("Escoge una opcion: "))
cpu = random.randint(1,3)

print(cpu)

if usuario == cpu:
    print("Empate")
elif (usuario == 1) & (cpu == 3):
    print("Ganaste")
elif (usuario == 2) & (cpu == 1):
    print("Ganaste")
elif (usuario == 3) & (cpu == 2):
    print("Ganaste")
else:
    print("Perdiste")
    
