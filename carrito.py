from excepciones import CantidadInvalidaError, ProductoNoEncontradoError, CarritoVacioError, ArchivoError
from datetime import datetime


class Carrito:
    def __init__(self):
        self._items = []

    def agregar(self, catalogo, id_producto, cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise CantidadInvalidaError(cantidad)
        producto = catalogo.obtener(id_producto)
        for item in self._items:
            if item["producto"].id_producto == id_producto:
                item["cantidad"] += cantidad
                return
        self._items.append({"producto": producto, "cantidad": cantidad})

    def listar(self):
        if not self._items:
            print("  (El carrito está vacío)")
            return
        print(f"{'Producto':<20} {'Cantidad':>8} {'Precio Unit.':>12} {'Subtotal':>10}")
        print("-" * 52)
        for item in self._items:
            p = item["producto"]
            cant = item["cantidad"]
            subtotal = p.precio * cant
            print(f"{p.nombre:<20} {cant:>8} ${p.precio:>8.2f} ${subtotal:>7.2f}")
        print("-" * 52)
        print(f"{'TOTAL':>40} ${self.calcular_total():>7.2f}")

    def calcular_total(self):
        return sum(item["producto"].precio * item["cantidad"] for item in self._items)

    def vaciar(self):
        self._items.clear()

    def esta_vacio(self):
        return len(self._items) == 0

    def confirmar_compra(self, ruta_archivo="ordenes.txt"):
        if self.esta_vacio():
            raise CarritoVacioError()
        try:
            with open(ruta_archivo, "a", encoding="utf-8") as f:
                f.write(f"=== ORDEN {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
                for item in self._items:
                    p = item["producto"]
                    cant = item["cantidad"]
                    subtotal = p.precio * cant
                    f.write(f"{p.nombre} | {cant} x ${p.precio:.2f} = ${subtotal:.2f}\n")
                total = self.calcular_total()
                f.write(f"TOTAL: ${total:.2f}\n\n")
        except OSError as e:
            raise ArchivoError(ruta_archivo, "escribir") from e
        self.vaciar()
        return total
