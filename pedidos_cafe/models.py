from django.db import models

# Create your models here.


class PedidoCafe(models.Model):
    cliente = models.CharField(max_length=100)
    tipo_base = models.CharField(
        max_length=20,
        choices=[
            ("espresso", "Espresso"),
            ("americano", "Americano"),
            ("latte", "Latte"),
        ],
    )
    ingredientes = models.JSONField(default=list, blank=True)
    tamanio = models.CharField(
        max_length=10,
        choices=[
            ("pequeño", "Pequeño"),
            ("mediano", "Mediano"),
            ("grande", "Grande"),
        ],
    )
    fecha = models.DateTimeField(auto_now_add=True)