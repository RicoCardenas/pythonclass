texto_reemplazar = "hola"

usuario = input("ingrese una letra: ")

if usuario in texto_reemplazar:
    print("si esta")
    buscar_letra = texto_reemplazar.find(usuario)
    nueva_palabra = texto_reemplazar.replace(texto_reemplazar[0], usuario)
    print(nueva_palabra)