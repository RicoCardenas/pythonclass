lista = ["Hola", "Mi", "Nombre", "Es", "Julian", "Tengo", 7, "Años"]

for i in lista:
    if isinstance(i, int):  # Verificar si el elemento es un número
        es_primo = True
        if i < 2:
            es_primo = False
        else:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    es_primo = False
                    break
        if es_primo:
            print(f"{i} es un número primo")
        else:
            print(f"{i} no es un numero primo")
    print(i)

