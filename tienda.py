from catalogo import Catalogo
from carrito import Carrito
from usuario import Admin, Cliente
from excepciones import ArchivoError


class Tienda:
    def __init__(self):
        self.catalogo = Catalogo()
        self.carrito = Carrito()

    def iniciar(self):
        print("=" * 50)
        print("         BIENVENIDO A LA TIENDA")
        print("=" * 50)

        try:
            self.catalogo.cargar()
            print("Catálogo")
        except ArchivoError as e:
            print(f"Advertencia: {e}")
        except Exception:
            pass

        if not self.catalogo._productos:
            self.catalogo.cargar_por_defecto()
            print("Catálogo.")

        while True:
            print("\n=== INICIO ===")
            print("1. Acceder como ADMIN")
            print("2. Acceder como CLIENTE")
            print("3. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                admin = Admin()
                admin.menu(self)
            elif opcion == "2":
                cliente = Cliente()
                cliente.menu(self)
            elif opcion == "3":
                print("¡Gracias por visitarnos!")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
