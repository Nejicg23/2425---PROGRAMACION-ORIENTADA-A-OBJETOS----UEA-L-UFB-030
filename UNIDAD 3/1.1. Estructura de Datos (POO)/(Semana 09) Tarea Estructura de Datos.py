
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    # Setters
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor

    @precio.setter
    def precio(self, valor):
        self._precio = valor

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | Cant: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.id == producto.id for p in self.productos):
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto(self, id):
        for i, p in enumerate(self.productos):
            if p.id == id:
                del self.productos[i]
                return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.id == id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                return True
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_inventario(self):
        for p in self.productos:
            print(p)


def mostrar_menu():
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario completo")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                nuevo_producto = Producto(id, nombre, cantidad, precio)
                if inventario.añadir_producto(nuevo_producto):
                    print("Producto añadido exitosamente!")
                else:
                    print("Error: ID ya existe")
            except ValueError:
                print("Error: Valores inválidos")

        elif opcion == "2":
            try:
                id = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id):
                    print("Producto eliminado!")
                else:
                    print("ID no encontrado")
            except ValueError:
                print("ID debe ser número")

        elif opcion == "3":
            try:
                id = int(input("ID del producto a actualizar: "))
                nueva_cant = input("Nueva cantidad (dejar vacío para mantener): ")
                nuevo_precio = input("Nuevo precio (dejar vacío para mantener): ")

                cantidad = int(nueva_cant) if nueva_cant else None
                precio = float(nuevo_precio) if nuevo_precio else None

                if inventario.actualizar_producto(id, cantidad, precio):
                    print("Actualización exitosa!")
                else:
                    print("ID no encontrado")
            except ValueError:
                print("Valores inválidos")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("\nResultados:")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos")

        elif opcion == "5":
            print("\nINVENTARIO COMPLETO")
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()