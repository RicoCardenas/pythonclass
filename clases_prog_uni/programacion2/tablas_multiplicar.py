numero = int(input("Ingresa el numero a multiplicar: "))
can_mult = int(input("Hasta donde desea que se multiplique: "))

for i in range(1, can_mult + 1):
    multiplicar = numero * i
    print (f"{numero} * {i} = {multiplicar}")