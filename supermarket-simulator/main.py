from clientes import Cliente

def main():
    cliente1 = Cliente(carrito = [])
    print(cliente1.nombre)    
    print("La aplicacion ha iniciado")
    while True:
        print("1. Agregar producto")
        

if __name__ == '__main__':
    main()