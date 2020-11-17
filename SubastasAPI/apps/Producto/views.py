from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
# Create your views here.
class ListaProductos(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class= ProductoSerializer

