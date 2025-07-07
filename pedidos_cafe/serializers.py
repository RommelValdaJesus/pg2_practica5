from rest_framework import serializers
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.factory import CafeFactory
from pedidos_cafe.builder import CafePersonalizadoBuilder, CafeDirector
from api_patrones.logger import Logger


class PedidoCafeSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCafe
        fields = [
            "id",
            "cliente",
            "tipo_base",
            "ingredientes",
            "tamanio",
            "fecha",
            "precio_total",
            "ingredientes_finales",
        ]

    INGREDIENTES_VALIDOS = {
        "canela": 1,
        "chocolate": 2,
        "vainilla": 1.5,
        "azucar": 0.5,
        "leche extra": 2
    }
    def validate_ingredientes(self, value):
        if value is None:
            return value
        
        if not isinstance(value, list):
            raise serializers.ValidationError("Los ingredientes deben ser una lista.")
        
        ingredientes_invalidos = [
            ingrediente for ingrediente in value if ingrediente not in self.INGREDIENTES_VALIDOS
        ]
        if ingredientes_invalidos:
            raise serializers.ValidationError(
                f"Los siguientes ingredientes no son válidos: {', '.join(ingredientes_invalidos)}"
            )
        return value


    def _build_cafe_and_get_builder(self, obj):
        if not obj.ingredientes:
         return None 
        # Patron Factory
        cafe = CafeFactory.obtener_base(obj.tipo_base)
        # Patron Builder
        builder = CafePersonalizadoBuilder(cafe)
        director = CafeDirector(builder)
        director.construir(obj.ingredientes, obj.tamanio)
        return builder  
    

    def get_precio_total(self, obj):
        if not obj.ingredientes:
            return 0.0  # o None, según el comportamiento deseado
        builder = self._build_cafe_and_get_builder(obj)
        Logger().registrar(f"Se registró el cálculo del precio para el pedido {obj.id}")
        return builder.obtener_precio()

    def get_ingredientes_finales(self, obj):
        if not obj.ingredientes:
            return []
        builder = self._build_cafe_and_get_builder(obj)
        Logger().registrar(f"Se registró la obtención de ingredientes finales para el pedido {obj.id}")
        return builder.obtener_ingredientes_finales()