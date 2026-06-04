from producto import Producto
from excepciones import ProductoNoEncontradoError, ArchivoError


class Catalogo:
    def __init__(self):
        self._productos = {}

    def listar(self):
        if not self._productos:
            print("  (El catálogo está vacío)")
            return
        print(f"{'ID':>3} | {'Nombre':<20} | {'Categoría':<15} | {'Precio':>8}")
        print("-" * 55)
        for p in self._productos.values():
            print(p)

    def obtener(self, id_producto):
        if id_producto not in self._productos:
            raise ProductoNoEncontradoError(id_producto)
        return self._productos[id_producto]

    def crear(self, producto):
        self._productos[producto.id_producto] = producto

    def actualizar(self, id_producto, nombre=None, categoria=None, precio=None):
        producto = self.obtener(id_producto)
        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio

    def eliminar(self, id_producto):
        if id_producto not in self._productos:
            raise ProductoNoEncontradoError(id_producto)
        del self._productos[id_producto]

    def buscar(self, texto=""):
        texto = texto.lower()
        resultados = [
            p for p in self._productos.values()
            if texto in p.nombre.lower() or texto in p.categoria.lower()
        ]
        return resultados

    def guardar(self, ruta_archivo="catalogo.txt"):
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write("id,nombre,categoria,precio\n")
                for p in self._productos.values():
                    f.write(p.to_csv() + "\n")
        except OSError as e:
            raise ArchivoError(ruta_archivo, "escribir") from e

    def cargar(self, ruta_archivo="catalogo.txt"):
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                next(f)
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        p = Producto.from_csv(linea)
                        self._productos[p.id_producto] = p
        except FileNotFoundError:
            pass
        except OSError as e:
            raise ArchivoError(ruta_archivo, "leer") from e

    def cargar_por_defecto(self):
        productos_iniciales = [
            Producto("P1", "Computador Escritorio", "Electrónica", 1000000),
            Producto("P2", "Mouse RGB", "Electrónica", 10000),
            Producto("P3", "Teclado Mecánico", "Electrónica", 40000),
            Producto("P4", "Monitor Pc", "Electrónica", 200000),
            Producto("P5", "Cafetera", "Hogar", 139000),
            Producto("P6", "Escritorio", "Muebles", 95000),
            Producto("P7", "Silla Gamer", "Muebles", 80000),
            Producto("P8", "Audífonos Gamer", "Electrónica", 40000),
            ]
        for p in productos_iniciales:
            self._productos[p.id_producto] = p
