import random

lista_palabras = ["abandonar", "abatido", "abeja", "abismo", "abrir", "absorber", "abuelo", "aceptar", "acierto", "acordeón", "actitud", "activo", "adelante", "adivinar", "adolescente", "adorable", "adornar", "adversario", "afable", "afectar", "afición", "agradable", "agradecer", "aguardar", "agua", "agudo", "ahijado", "ahogar", "ahorrar", "bailar", "bajar", "banco", "barco", "barrera", "básico", "bastar", "bello", "bendecir", "besar", "bienestar", "boca", "bondad", "borrar", "bravo", "brazo", "brillar", "brote", "buscar", "búho", "burlar", "buzón", "cabello", "caer", "caja", "calma", "cambiar", "candado", "canto", "capaz", "capítulo", "carácter", "cargar", "cariño", "carta", "casar", "castigar", "causa", "cazar", "ceder", "celebrar", "celoso", "cementerio", "ceniza", "centro", "cerca", "cerrar", "cielo", "cifra", "círculo", "claro", "dar", "dato", "deber", "dejar", "delgado", "demás", "dentro", "depender", "derecho", "desde", "desear", "desnudo", "despacio", "destino", "destruir", "detener", "devolver", "dibujo", "dicho", "diente", "difícil", "digno", "dinero", "dios", "dirección", "dirigir", "discurso", "doble", "dolor", "echar", "edad", "edificio", "educar", "efecto", "ejemplo", "eje", "elección", "elegir", "elemento", "elevar", "eliminar", "ello", "embargo", "empezar", "empleado", "emplear", "empresa", "enemigo", "enfadar", "enfermo", "engañar", "enlace", "enorme", "enseñar", "entero", "entonces", "entrada", "entretenido","fácil", "falta", "familia", "fanático", "fantasma", "felicidad", "feliz", "femenino", "fiebre", "fiel", "fiesta", "figura", "fijar", "final", "finanzas", "fingir", "firma", "flecha", "flor", "florecer", "fondo", "forma", "formar", "fortuna", "frente", "fresco", "fuego", "fuerte", "fumar", "ganar", "gato", "general", "genio", "gente", "gesto", "golpear", "gracia", "grande", "gratis", "gritar", "grupo", "guardar", "guerra", "guía", "gusto", "gustar", "guzmán", "hablar", "habitación", "hablar", "hacer", "hacia", "hallar", "hambre", "hacer", "hermano", "hermoso", "héroe", "hijo", "historia", "hogar", "hora", "hombre", "hombro", "honor", "horror", "hoy", "huevo", "humano", "humilde", "humor", "hundir", "huésped", "huir", "hueso", "huevo", "ideal", "identidad", "idioma", "iglesia", "imagen", "imaginar", "impedir", "imperio", "imponer", "importar", "imprimir", "incluir", "incluso", "increíble", "indio", "informar", "ingenio", "ingresar", "iniciar", "injusto", "inmediato", "inocente", "inquieto", "insistir", "instalar", "instituto", "instruir", "inteligente", "intentar", "jardín", "jefe", "joven", "juego", "jugar", "junto", "jurar", "justo", "kilómetro", "kilo", "kiwi", "labor", "lado", "lamentar", "largo", "lágrima", "lamentar", "lápiz", "largo", "largo", "lección", "leer", "lengua", "levantar", "libertad", "libre", "libro", "líder", "ligero", "limpiar", "lindo", "línea", "listo", "llegar", "llorar", "lluvia", "loco", "lograr", "lugar", "luz", "madre", "mágico", "maldad", "malo", "máquina", "mar", "marchar", "máscara", "masivo", "matar", "materia", "máximo", "médico", "medida", "medio", "mejor", "memoria", "menor", "mentir", "mensaje", "mente", "menú", "mercado", "mermelada", "mesa", "metal", "meter", "miedo", "miel", "militar", "millón", "minuto", "mismo", "mitad", "modelo", "moderno", "molestar", "momento", "moneda", "monstruo", "mostrar", "motivo", "mover", "mujer", "mundo", "música", "nacer", "nación", "nadar", "naranja", "narrar", "natural", "necesario", "negar", "negocio", "ñandú", "ñeque", "ñato", "oasis", "objeto", "obra", "obtener", "ocasión", "ocultar", "ocurrir", "ofender", "oferta", "ofrecer", "oído", "ojalá", "ojo", "ola", "oleada", "oler", "olfato", "olvidar", "onda", "opinar", "oportunidad", "opuesto", "orden", "oreja", "orgullo", "origen", "oro", "oso", "otro", "página", "país", "padre", "página", "palabra", "palacio", "palma", "paloma", "palpar", "pan", "panza", "papel", "par", "parar", "pared", "pareja", "parque", "parte", "partir", "pasar", "paso", "pastel", "patio", "paz", "pecado", "pecho", "pedir", "pegar", "pelar", "quedarse", "querer", "quitar", "rápido", "raro", "razón", "real", "realidad", "rechazar", "recibir", "reclamar", "recoger", "reconocer", "recordar", "recto", "reducir", "referir", "reflejar", "refugiar", "regalar", "región", "regla", "regresar", "regular", "reír", "relación", "relajar", "religión", "reloj", "remedio", "remover", "saber", "sábado", "sacar", "sacudir", "sagrado", "sal", "sala", "salir", "salud", "salvar", "sangre", "sano", "santo", "sapo", "satisfacer", "seco", "secreto", "seguir", "seguro", "seis", "semana", "semilla", "señalar", "señor", "sentido", "sentir", "separar", "ser", "serio", "tamaño", "también", "tampoco", "tanque", "tapa", "tardar", "tarde", "tarea", "tarifa", "tarjeta", "taza", "techo", "tejido", "televisor", "tema", "temer", "temor", "templo", "tener", "teoría", "terapia", "terco", "terminar", "término", "tesoro", "testigo", "texto", "tiempo", "tienda", "último", "único", "unidad", "unir", "uno", "uña", "urbano", "urgente", "urgir", "urna", "usar", "uso", "útil", "utilizar", "utopía", "útil", "utilizar", "utopía", "uva", "vaca", "vaciar", "vagar", "valer", "valiente", "valor", "vampiro", "vapor", "vara", "varón", "vaso", "veinte", "vejez", "vela", "veloz", "vencer", "vender", "venir", "ventana", "ver", "verano", "verbo", "verde", "verdad", "verdugo", "verter", "vestir", "vez", "vibrar", "waffle", "wáter", "websites", "xenofobia", "xenón", "xilófono"]

palabra_cpu = random.choice(lista_palabras)
vidas = 6

print(palabra_cpu)

# funcion que retorna la longitud de la palabra
def tamaño_palabra():
    return len(palabra_cpu)

#funcion que convierte la palabra elegida de la cpu en guiones
def convertir_guiones():
    return palabra_cpu.replace(palabra_cpu, "-" * tamaño_palabra())

name_usr = input("ingresa tu nombre: ")

def mensaje():
    return f"\nHola {name_usr} hoy jugaremos a EL AHORCADO\nsupongo que sabes como funciona este juego, asi que entonces tienes 6 vidas para adivinar la palabra, cada que falles una letra, perderas una vida, es importante que sepas de ortografia si la palabra secreta contiene una (á) sera diferente de una (a), asi que....\nMUCHA SUERTE!!"

def mostrar_guiones():
    return f"la palabra secreta tiene {tamaño_palabra()} letras y es la siguiente:\n{convertir_guiones()}"

def letras_usr():
    letra_usr = input("\nIngresa una letra: ").lower()
    return letra_usr

def verificar_letra():
    convertir_guiones()
    letras_usr()
    if letras_usr() in palabra_cpu:
        print(f"La letra {letras_usr()} se encuentra {palabra_cpu.count(letras_usr())} vez/veces en la palabra secreta, muy bien!!!")
        guiones_list = list(convertir_guiones())
        print(guiones_list)
        for i in range(len(palabra_cpu)):
            if palabra_cpu[i] == letras_usr():
                guiones_list[i] = letras_usr()
        nueva_palabra = "".join(guiones_list)
        print(nueva_palabra)
        return nueva_palabra
    
print(mensaje())
verificar_letra()

    
