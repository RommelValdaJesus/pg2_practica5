# Python native imports
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from pedidos_cafe.serializers import *
from pedidos_cafe.models import *
from django.conf import settings


class PedidoCafeViewSet(viewsets.ModelViewSet):
    queryset = PedidoCafe.objects.all().order_by("-fecha")
    serializer_class = PedidoCafeSerializer