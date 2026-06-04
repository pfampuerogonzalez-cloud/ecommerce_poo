class Producto:
    def __init__(self, id_producto, nombre, categoria, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto:>3} | {self.nombre:<20} | {self.categoria:<15} | ${self.precio:>7.2f}"

    def to_csv(self):
        return f"{self.id_producto},{self.nombre},{self.categoria},{self.precio}"

    @staticmethod
    def from_csv(linea):
        id_producto, nombre, categoria, precio = linea.strip().split(",")
        return Producto(id_producto, nombre, categoria, float(precio))
