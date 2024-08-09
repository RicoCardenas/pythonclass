import time
def agregar_producto(carrito, producto, precio, cantidad):
    carrito.append({'producto': producto, 
                    'precio': precio,
                    'cantidad': cantidad
                    })

def valor_total(carrito):
    total = 0
    for item in carrito:
        total += item['cantidad']*item['precio']
    return total

def ver_carrito(carrito):
    print("-----------------------------")
    for item in carrito:
        valor_acumulado = item['precio']*item['cantidad']
        print(f"{item['producto']} - ${item['precio']} * {item['cantidad']} = ${valor_acumulado}")
    print(f"Total: ${valor_total(carrito)}")
    print("-----------------------------")
    
def eliminar_producto(carrito, producto):
    print("Desea eliminar uan cantidad o producto?")
    print("1. Cantidad")
    print("2. Producto")
    opcion = int(input("Selecciona la opcion: "))
    if opcion == 1:
        producto = input("Introduce el nombre del producto: ").capitalize()
        if producto in [item['producto'] for item in carrito]: 
            cantidad = int(input("Introduce la cantidad a eliminar: "))
            for item in carrito:
                if item['producto'] == producto:
                    item['cantidad'] -= cantidad
                    print(f"{cantidad} {producto} eliminado del carrito")
                    break
        else: 
            print("Producto no encontrado")
    elif opcion == 2:        
        producto = input("Introduce el nombre del producto a eliminar: ").capitalize()
        for item in carrito:
            if item['producto'] == producto:
                carrito.remove(item)
                print(f"{producto} eliminado del carrito")
                break
            else:
                print("Producto no encontrado")
    else: 
        print("Opcion no valida")    

def pagar(carrito, dinero):
    dinero = float(input(f"Con cuanto vas a pagar: "))
    total = valor_total(carrito)
    cambio = dinero - total
    if dinero < total:
        print("Cantidad insuficiente")
    elif dinero == total:
        print("No hay cambio")
        print("Gracias por su compra")
    else:
        print("--------------------------------------") 
        print("Factura")
        ver_carrito(carrito)
        print(f"Paga con: ${dinero}")    
        print(f"Tu cambio es de ${cambio}")
        print("Gracias por su compra\nVuelva pronto....")
        print("--------------------------------------")    
    
def main():
    dinero = 0
    carrito = []
    print(f"Bienvenido al supermercado PUTITOS")
    while True:
        print(f"1. Agregar producto")
        print(f"2. Ver carrito")
        print(f"3. Pagar")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = int(input("Selecciona la opcion: "))
        if opcion == 1:
            producto = input("introduce el nombre del producto: ").capitalize()
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad del producto: "))
            agregar_producto(carrito, producto, precio, cantidad)
        elif opcion == 2:
            ver_carrito(carrito)  
        elif opcion == 3:
            pagar(carrito, dinero)
            time.sleep(3)
            break
        elif opcion == 4:
            eliminar_producto(carrito, producto)
        elif opcion == 5:
            break
        else: 
            print("Opcion no valida")
    
if __name__ == "__main__" :
    main()    