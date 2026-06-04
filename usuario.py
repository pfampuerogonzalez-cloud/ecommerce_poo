from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def menu(self, tienda):
        pass


class Admin(Usuario):
    def __init__(self, nombre="Administrador"):
        super().__init__(nombre)

    def menu(self, tienda):
        from excepciones import ProductoNoEncontradoError, ArchivoError
        from producto import Producto

        while True:
            print(f"\n=== MENÚ ADMIN ({self.nombre}) ===")
            print("1. Listar productos")
            print("2. Crear producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Guardar catálogo en archivo")
            print("6. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                tienda.catalogo.listar()

            elif opcion == "2":
                try:
                    id_p = input("ID del producto: ").strip()
                    nombre = input("Nombre: ").strip()
                    categoria = input("Categoría: ").strip()
                    precio = float(input("Precio: ").strip())
                    tienda.catalogo.crear(Producto(id_p, nombre, categoria, precio))
                    print("Producto creado correctamente.")
                except ValueError:
                    print("Error: el precio debe ser un número.")

            elif opcion == "3":
                try:
                    tienda.catalogo.listar()
                    id_p = input("ID del producto a actualizar: ").strip()
                    print("Deja en blanco para mantener el valor actual.")
                    nombre = input("Nuevo nombre: ").strip() or None
                    categoria = input("Nueva categoría: ").strip() or None
                    precio_str = input("Nuevo precio: ").strip()
                    precio = float(precio_str) if precio_str else None
                    tienda.catalogo.actualizar(id_p, nombre, categoria, precio)
                    print("Producto actualizado correctamente.")
                except ProductoNoEncontradoError as e:
                    print(f"Error: {e}")
                except ValueError:
                    print("Error: el precio debe ser un número.")

            elif opcion == "4":
                try:
                    tienda.catalogo.listar()
                    id_p = input("ID del producto a eliminar: ").strip()
                    tienda.catalogo.eliminar(id_p)
                    print("Producto eliminado correctamente.")
                except ProductoNoEncontradoError as e:
                    print(f"Error: {e}")

            elif opcion == "5":
                try:
                    tienda.catalogo.guardar()
                    print("Catálogo guardado en 'catalogo.txt'.")
                except ArchivoError as e:
                    print(f"Error: {e}")

            elif opcion == "6":
                print("Saliendo del menú ADMIN.")
                return
            else:
                print("Opción inválida. Intenta de nuevo.")


class Cliente(Usuario):
    def __init__(self, nombre="Cliente"):
        super().__init__(nombre)

    def menu(self, tienda):
        from excepciones import CantidadInvalidaError, ProductoNoEncontradoError, CarritoVacioError, ArchivoError

        carrito = tienda.carrito

        while True:
            print(f"\n=== MENÚ CLIENTE ({self.nombre}) ===")
            print("1. Ver catálogo")
            print("2. Buscar productos")
            print("3. Agregar producto al carrito")
            print("4. Ver carrito")
            print("5. Confirmar compra")
            print("6. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                tienda.catalogo.listar()

            elif opcion == "2":
                texto = input("Buscar (nombre o categoría): ").strip()
                resultados = tienda.catalogo.buscar(texto)
                if not resultados:
                    print("No se encontraron productos.")
                else:
                    for p in resultados:
                        print(p)

            elif opcion == "3":
                try:
                    tienda.catalogo.listar()
                    id_p = input("ID del producto: ").strip()
                    cant = int(input("Cantidad: ").strip())
                    carrito.agregar(tienda.catalogo, id_p, cant)
                    print("Producto agregado al carrito.")
                except ProductoNoEncontradoError as e:
                    print(f"Error: {e}")
                except CantidadInvalidaError as e:
                    print(f"Error: {e}")
                except ValueError:
                    print("Error: la cantidad debe ser un número entero.")

            elif opcion == "4":
                carrito.listar()

            elif opcion == "5":
                try:
                    total = carrito.confirmar_compra()
                    print(f"Compra confirmada. Total pagado: ${total:.2f}")
                    print("La orden se ha registrado en 'ordenes.txt'.")
                except CarritoVacioError as e:
                    print(f"Error: {e}")
                except ArchivoError as e:
                    print(f"Error: {e}")

            elif opcion == "6":
                print("Saliendo del menú CLIENTE.")
                return
            else:
                print("Opción inválida. Intenta de nuevo.")
