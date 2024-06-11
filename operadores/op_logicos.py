#AND
resultado1 = True & True #True
resultado2 = True & False #False
resultado3 = False & True #False
resultado4 = False & False #False

#OR
resultado5 = True | True #True
resultado6 = True | False #True
resultado7 = False | True #True
resultado8 = False | False #False
#NOT

resultado9 = not True #False
resultado10 = not False #True

for i in range(1,11):
    print(f"El resultado {i} es: ")
    print(eval(f"resultado{i}"))
#NOTA: En Python se pueden usar los operadores & y | para hacer operaciones logicas, pero tambien se pueden usar and y or

for i in range(10):
    print(i+1)