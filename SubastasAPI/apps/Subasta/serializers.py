from rest_framework.serializers import ModelSerializer
from .models import Oferta
class OfertaSerializer(ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['NombreProducto', 'Estado','Precio_final']