import random

lista_nombres = ['Juan', 'Pedro', 'Maria', 'Jose', 'Ana', 'Luis', 'Carlos', 'Andres', 'Sofia', 'Lucia']

class Cliente: 
    def __init__(self, carrito):
        self.nombre = random.choice(lista_nombres)
        self.carrito = carrito
        
    def agregar_producto(self, producto, precio):
        self.carrito.append({'producto': producto, 'precio': precio})
        
    def mostrar_carrito(self):
        for producto in self.carrito:
            print(producto['producto'], producto['precio'])