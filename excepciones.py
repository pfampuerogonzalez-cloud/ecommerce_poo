class ProductoNoEncontradoError(Exception):
    def __init__(self, id_producto):
        super().__init__(f"Producto con ID '{id_producto}' no encontrado en el catálogo.")
        self.id_producto = id_producto


class CantidadInvalidaError(Exception):
    def __init__(self, cantidad):
        super().__init__(f"Cantidad inválida: '{cantidad}'. Debe ser un entero positivo.")
        self.cantidad = cantidad


class CarritoVacioError(Exception):
    def __init__(self):
        super().__init__("El carrito está vacío. Agrega productos para realizar la compra.")


class ArchivoError(Exception):
    def __init__(self, archivo, operacion):
        super().__init__(f"No se pudo {operacion} el archivo '{archivo}'.")
        self.archivo = archivo
        self.operacion = operacion
