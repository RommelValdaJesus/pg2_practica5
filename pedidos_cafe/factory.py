from pedidos_cafe.base import Espresso, Americano, Latte


class CafeFactory:
    @staticmethod
    def obtener_base(tipo):
        if tipo == "espresso":
            cafe = Espresso()
        elif tipo == "americano":
            cafe = Americano()
        elif tipo == "latte":
            cafe = Latte()
        else:
            raise ValueError("Tipo de café no válido")

        cafe.inicializar()
        return cafe