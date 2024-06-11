#primero creamos una lista con 1000 palabras de 6 letras cada una
import random

lista_palabras = ["abandonar", "abatido", "abeja", "abismo", "abrir", "absorber", "abuelo", "aceptar", "acierto", "acordeón", "actitud", "activo", "adelante", "adivinar", "adolescente", "adorable", "adornar", "adversario", "afable", "afectar", "afición", "agradable", "agradecer", "aguardar", "agua", "agudo", "ahijado", "ahogar", "ahorrar", "bailar", "bajar", "banco", "barco", "barrera", "básico", "bastar", "bello", "bendecir", "besar", "bienestar", "boca", "bondad", "borrar", "bravo", "brazo", "brillar", "brote", "buscar", "búho", "burlar", "buzón", "cabello", "caer", "caja", "calma", "cambiar", "candado", "canto", "capaz", "capítulo", "carácter", "cargar", "cariño", "carta", "casar", "castigar", "causa", "cazar", "ceder", "celebrar", "celoso", "cementerio", "ceniza", "centro", "cerca", "cerrar", "cielo", "cifra", "círculo", "claro", "dar", "dato", "deber", "dejar", "delgado", "demás", "dentro", "depender", "derecho", "desde", "desear", "desnudo", "despacio", "destino", "destruir", "detener", "devolver", "dibujo", "dicho", "diente", "difícil", "digno", "dinero", "dios", "dirección", "dirigir", "discurso", "doble", "dolor", "echar", "edad", "edificio", "educar", "efecto", "ejemplo", "eje", "elección", "elegir", "elemento", "elevar", "eliminar", "ello", "embargo", "empezar", "empleado", "emplear", "empresa", "enemigo", "enfadar", "enfermo", "engañar", "enlace", "enorme", "enseñar", "entero", "entonces", "entrada", "entretenido","fácil", "falta", "familia", "fanático", "fantasma", "felicidad", "feliz", "femenino", "fiebre", "fiel", "fiesta", "figura", "fijar", "final", "finanzas", "fingir", "firma", "flecha", "flor", "florecer", "fondo", "forma", "formar", "fortuna", "frente", "fresco", "fuego", "fuerte", "fumar", "ganar", "gato", "general", "genio", "gente", "gesto", "golpear", "gracia", "grande", "gratis", "gritar", "grupo", "guardar", "guerra", "guía", "gusto", "gustar", "guzmán", "hablar", "habitación", "hablar", "hacer", "hacia", "hallar", "hambre", "hacer", "hermano", "hermoso", "héroe", "hijo", "historia", "hogar", "hora", "hombre", "hombro", "honor", "horror", "hoy", "huevo", "humano", "humilde", "humor", "hundir", "huésped", "huir", "hueso", "huevo", "ideal", "identidad", "idioma", "iglesia", "imagen", "imaginar", "impedir", "imperio", "imponer", "importar", "imprimir", "incluir", "incluso", "increíble", "indio", "informar", "ingenio", "ingresar", "iniciar", "injusto", "inmediato", "inocente", "inquieto", "insistir", "instalar", "instituto", "instruir", "inteligente", "intentar", "jardín", "jefe", "joven", "juego", "jugar", "junto", "jurar", "justo", "kilómetro", "kilo", "kiwi", "labor", "lado", "lamentar", "largo", "lágrima", "lamentar", "lápiz", "largo", "largo", "lección", "leer", "lengua", "levantar", "libertad", "libre", "libro", "líder", "ligero", "limpiar", "lindo", "línea", "listo", "llegar", "llorar", "lluvia", "loco", "lograr", "lugar", "luz", "madre", "mágico", "maldad", "malo", "máquina", "mar", "marchar", "máscara", "masivo", "matar", "materia", "máximo", "médico", "medida", "medio", "mejor", "memoria", "menor", "mentir", "mensaje", "mente", "menú", "mercado", "mermelada", "mesa", "metal", "meter", "miedo", "miel", "militar", "millón", "minuto", "mismo", "mitad", "modelo", "moderno", "molestar", "momento", "moneda", "monstruo", "mostrar", "motivo", "mover", "mujer", "mundo", "música", "nacer", "nación", "nadar", "naranja", "narrar", "natural", "necesario", "negar", "negocio", "ñandú", "ñeque", "ñato", "oasis", "objeto", "obra", "obtener", "ocasión", "ocultar", "ocurrir", "ofender", "oferta", "ofrecer", "oído", "ojalá", "ojo", "ola", "oleada", "oler", "olfato", "olvidar", "onda", "opinar", "oportunidad", "opuesto", "orden", "oreja", "orgullo", "origen", "oro", "oso", "otro", "página", "país", "padre", "página", "palabra", "palacio", "palma", "paloma", "palpar", "pan", "panza", "papel", "par", "parar", "pared", "pareja", "parque", "parte", "partir", "pasar", "paso", "pastel", "patio", "paz", "pecado", "pecho", "pedir", "pegar", "pelar", "quedarse", "querer", "quitar", "rápido", "raro", "razón", "real", "realidad", "rechazar", "recibir", "reclamar", "recoger", "reconocer", "recordar", "recto", "reducir", "referir", "reflejar", "refugiar", "regalar", "región", "regla", "regresar", "regular", "reír", "relación", "relajar", "religión", "reloj", "remedio", "remover", "saber", "sábado", "sacar", "sacudir", "sagrado", "sal", "sala", "salir", "salud", "salvar", "sangre", "sano", "santo", "sapo", "satisfacer", "seco", "secreto", "seguir", "seguro", "seis", "semana", "semilla", "señalar", "señor", "sentido", "sentir", "separar", "ser", "serio", "tamaño", "también", "tampoco", "tanque", "tapa", "tardar", "tarde", "tarea", "tarifa", "tarjeta", "taza", "techo", "tejido", "televisor", "tema", "temer", "temor", "templo", "tener", "teoría", "terapia", "terco", "terminar", "término", "tesoro", "testigo", "texto", "tiempo", "tienda", "último", "único", "unidad", "unir", "uno", "uña", "urbano", "urgente", "urgir", "urna", "usar", "uso", "útil", "utilizar", "utopía", "útil", "utilizar", "utopía", "uva", "vaca", "vaciar", "vagar", "valer", "valiente", "valor", "vampiro", "vapor", "vara", "varón", "vaso", "veinte", "vejez", "vela", "veloz", "vencer", "vender", "venir", "ventana", "ver", "verano", "verbo", "verde", "verdad", "verdugo", "verter", "vestir", "vez", "vibrar", "waffle", "wáter", "websites", "xenofobia", "xenón", "xilófono"]

#la cpu escoge una palabra al azar de la lista de palabras creada
palabra_cpu = random.choice(lista_palabras)

nombre = input("\nIngresa tu nombre: ").capitalize()
#el usuario tiene 6 intentos para adivinar la palabra
vidas = 6

#en la variable tamaño de palabra se almacena el tamaño de la palabra escogida por la cpu
tamaño_de_palabra = len(palabra_cpu)

print("--------------------------------------")
#se le informa al usuario las reglas del juego
print(f'''\nhola {nombre} hoy jugaremos a EL AHORCADO
supongo que sabes como funciona este juego, asi que entonces
tienes {vidas} vidas para adivinar la palabra,
cada que falles una letra, perderas una vida, es importante que sepas de ortografia
si la palabra secreta contiene una (á) sera diferente de una (a), asi que....
MUCHA SUERTE!!''')
print("\n--------------------------------------")

#se crea una cadena de guiones el cual va a ser del mismo tamaño que la palabra escogida por el usuario
palabra_guiones = "_" * tamaño_de_palabra
#se reemplaza la palabra de la cpu por la cadena de guiones
guiones = palabra_cpu.replace(palabra_cpu, palabra_guiones)


print(f"la palabra secreta tiene {tamaño_de_palabra} letras y es la siguiente:\n{guiones}")

def verificar_letra():
    global guiones
    global vidas
    #el bucle While se repetira siempre y cuando vidas sea mayor a 0, en el momento de llegar a 0 se terminara y perdera el usuario
    while vidas > 0:
        #Le pedimos al usuario que ingrese una letra
        letra_usr = input("\nIngresa una letra: ").lower()
        #el condicional if busca si la letra ingresada por el usuario esta en la palabra escogida por la CPU
        if letra_usr in palabra_cpu:
            print(f"La letra {letra_usr} se encuentra {palabra_cpu.count(letra_usr)} vez/veces en la palabra secreta, muy bien!!!")
            guiones_list = list(guiones) #La variable guiones_list se encarga de convertir nuestro String en una lista separada para asi poder reemplazar los datos
            for i in range(len(palabra_cpu)): #El bucle for se encarga de verificar si la letra ingresada por el usuario se repite en mas de una ocasion en la palabra secreta, si es asi, la reemplaza en los 2 espacio correspondientes
                if palabra_cpu[i] == letra_usr:
                    guiones_list[i] = letra_usr
            nueva_palabra = "".join(guiones_list) #Volvemos a unir nuestra lista en una cadena de texto
            print(nueva_palabra)
            guiones = nueva_palabra #Le damos a guiones el valor de nueva palabra para que se vaya guardando a medida que se repite el bucle
            if nueva_palabra == palabra_cpu:
                print("-------------------------------------")  
                print(f"\nFelicitaciones, {nombre} has ganado y quedaste con {vidas} vidas")
                print("\n-------------------------------------")
                break         
        else:
            print(f"Ou {nombre} has perdido una vida te quedan {vidas - 1}")
            vidas -= 1
            if vidas == 0:
                print(f"\nLa palabra secreta era {palabra_cpu}")
                print(f"Bueno {nombre} Haz perdido el juego vuelve a intentarlo")   
    
verificar_letra()    

