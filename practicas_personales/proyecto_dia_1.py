#pide al usuario ingresar un texto
texto_usuario = input("introduce el texto: ").lower()

#pide al usuario ingresar 3 letras de su seleccion
print("\nIngresa 3 letras de tu seleccion:")

letra_1 = input("\nIngresa la primera letra: ").lower()
letra_2 = input("Ingresa la segunda letra: ").lower()
letra_3 = input("Ingresa la tercera letra: ").lower()

cantidad_letras = list(texto_usuario)

print(f"\nla letra {letra_1} esta {cantidad_letras.count(letra_1)} veces en el texto \nla letra {letra_2} esta {cantidad_letras.count(letra_2)} veces en el texto \nla letra {letra_3} esta {cantidad_letras.count(letra_3)} veces en el texto")

longitud_texto = len(texto_usuario.split())
print(f"\nla cantidad de palabras en el texto es: {longitud_texto}")

#mostrar la primera y la ultima letra del texto ingresado por el usuario
primera_letra = texto_usuario[0]
ultima_letra = texto_usuario[-1]
print(f"\nla primera letra del texto es {primera_letra} y la ultima letra es {ultima_letra}")

#revertir texto
texto_revertido = texto_usuario[::-1]
print(f"\nel texto invertido es: {texto_revertido}")

#se encuentra la palabra python en el texto ingresado por el usuario??
palabra = "python"
if palabra.lower() in texto_usuario:
     palabra_python = True
else:
     palabra_python = False
     
print(f"\nse encuentra la palabra python? \n{palabra_python}")