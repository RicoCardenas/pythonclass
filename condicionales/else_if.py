ingreso_mensual = 100000
gasto_mensual = 97000

#if anidados else y else if(elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual <= 0:
        print("estas gastando mas de lo que ganas")
    elif ingreso_mensual - gasto_mensual >= 4000:
        print("estas ahorrando bien")
    else :
        print("hay que ver que te alcance")
elif ingreso_mensual >= 1000:
    print("estas bien en latinoamerica")
else:
    print("estas en la pobreza")