from rest_framework.serializers import ModelSerializer
from .models import Venta
class OfertaSerializer(ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['Fecha', 'Total','Subasta','Producto']