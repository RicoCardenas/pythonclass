lista = []

for i in range(1, 11):
    num = float(input("ingrese su numero: "))
    lista.append(num)

cont_pos=0
cont_neg=0
cont_cero=0
    
for num in lista:
    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    else:
        cont_cero += 1

print(f"La cantidad de numeros positivos es: {cont_pos}")
print(f"La cantidad de numeros negativos es: {cont_neg}")
print(f"La cantidad de ceros es: {cont_cero}")