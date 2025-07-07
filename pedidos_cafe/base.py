class CafeBase:
    def __init__(self):
        self.ingredientes = []
        self.precio = 0

    def inicializar(self):
        """Define los ingredientes y el precio base. Implementado por subclases."""
        raise NotImplementedError()

    def obtener_ingredientes_base(self):
        return self.ingredientes

    def precio_base(self):
        return self.precio


class Espresso(CafeBase):
    def inicializar(self):
        self.ingredientes = ["café concentrado"]
        self.precio = 10


class Americano(CafeBase):
    def inicializar(self):
        self.ingredientes = ["café filtrado", "agua caliente"]
        self.precio = 12


class Latte(CafeBase):
    def inicializar(self):
        self.ingredientes = ["café concentrado", "leche vaporizada", "espuma"]
        self.precio = 15