from django import forms
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.serializers import PedidoCafeSerializer


class PedidoCafeAdminForm(forms.ModelForm):
    class Meta:
        model = PedidoCafe
        fields = '__all__' 

    def clean_ingredientes(self):

        ingredientes = self.cleaned_data.get('ingredientes')
        
        if not isinstance(ingredientes, list):
            ingredientes = []

        ingredientes_permitidos = PedidoCafeSerializer.INGREDIENTES_VALIDOS.keys()

        for ingrediente in ingredientes:
            if ingrediente not in ingredientes_permitidos:
                raise forms.ValidationError(
                    f"Ingrediente '{ingrediente}' no válido o no disponible. "
                    f"Los permitidos son: {', '.join(ingredientes_permitidos)}"
                )
        return ingredientes