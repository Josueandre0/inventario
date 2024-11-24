#creacion de la clase
class Producto():

    #implementacion de las clases 
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    #getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad
    
    #Setters
    def set_precio(self,precio):
        if precio > 0:
            self.__precio = precio
        else:
            return ValueError("El precio debe ser mayor que 0")
        
    def set_cantidad(self,cantidad):
        if cantidad > 0:
            self.__cantidad = cantidad
        else:
            return ValueError("La cantidad debe ser mayor que 0")
        

 #Creacion clase inventario        
class Invetarario():
    def __init__(self):
        self.__productos = []  #lista para almacenar obejto clase Producto 

    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            print("El producto ya existe en el inventario")
        else:
            self.__productos.append(producto)
            print(f"prducto '{producto.get_nombre()}' agreado al inventario")

    def actualizar_inventario(self, nombre, precio=None, cantidad=None):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                if precio is not None:
                    producto.set_precio(precio)
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                print(f"Producto '{nombre}' actulizado")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario")

    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                print(f"Producto {nombre} eliminado del inventario")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario")

    def mostrar_inventario(self):
        if not self.__productos:
            print("el inventario esta vacio")
        else:
            print("Inventario:")
            for producto in self.__productos:
                print(f"Producto: Nombre: {producto.get_nombre()}, Categoria: {producto.get_categoria()}"
                      f"Precio: {producto.get_precio()}, Cantidad: {producto.get_cantidad()}")
                
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: Nombre: {producto.get_nombre()}, Categoria: {producto.get_categoria()}"
                      f"Precio: {producto.get_precio()}, Cantidad: {producto.get_cantidad()}")
                return
        print(f"Producto {nombre} no encontrado en el inventario")


#ejemplo de uso
if __name__ == "__main__":
    inventario = Invetarario()



#creamos un procuto
producto1 = Producto("manzana", "fruta", 20, 300)
producto2 = Producto("pera", "fruta", 4, 600)
producto3 = Producto("melocoton", "fruta", 39, 900)

#agregamos el producto
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

#mostrar inventario 
inventario.mostrar_inventario()

#antualizar inventario
inventario.actualizar_inventario("manzana",20, 500)

#buscar un producto 
inventario.buscar_producto("manzana")

#eliminar un producto
inventario.eliminar_producto("pera")

inventario.mostrar_inventario()

