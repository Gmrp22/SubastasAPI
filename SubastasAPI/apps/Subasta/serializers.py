from rest_framework.serializers import ModelSerializer
from .models import Subasta
class SubastaSerializer(ModelSerializer):
    class Meta:
        model = Subasta
        fields = ['id','NProducto', 'Estado','Precio_final']