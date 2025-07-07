class CafePersonalizadoBuilder:
    def __init__(self, cafe_base):
        self.base = cafe_base
        self.precio = cafe_base.precio_base()
        self.ingredientes = list(cafe_base.obtener_ingredientes_base())

    def agregar_ingrediente(self, ingrediente):
        precios = {
            "canela": 1,
            "chocolate": 2,
            "vainilla": 1.5,
            "azucar": 0.5,
            "leche extra": 2,
        }
        if ingrediente not in precios:
            raise ValueError(f"Ingrediente '{ingrediente}' no válido o no disponible.")
        self.ingredientes.append(ingrediente)
        self.precio += precios.get(ingrediente, 0)

    def ajustar_tamanio(self, tamaño):
        if tamaño == "mediano":
            self.precio *= 1.25
        elif tamaño == "grande":
            self.precio *= 1.5

    def obtener_precio(self):
        return round(self.precio, 2)

    def obtener_ingredientes_finales(self):
        return self.ingredientes


class CafeDirector:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, ingredientes, tamaño):
        for i in ingredientes:
            self.builder.agregar_ingrediente(i)
        self.builder.ajustar_tamanio(tamaño)

    def construir_paquete_1(self):
        self.builder.agregar_ingrediente("canela")
        self.builder.agregar_ingrediente("chocolate")
        self.builder.ajustar_tamanio("mediano")

    def construir_paquete_2(self):
        self.builder.agregar_ingrediente("vainilla")
        self.builder.agregar_ingrediente("azucar")
        self.builder.ajustar_tamanio("grande")

    def construir_paquete_3(self):
        self.builder.agregar_ingrediente("leche extra")
        self.builder.agregar_ingrediente("canela")
        self.builder.ajustar_tamanio("pequeño")