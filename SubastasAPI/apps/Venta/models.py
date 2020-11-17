from django.db import models
from apps.Subasta.models import Subasta
from apps.Producto.models import Producto
# Create your models here.
class Venta(models.Model):
    """ Modelo del producto"""
    Fecha = models.DateField()
    #Vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Total = models.FloatField()
    Subasta = models.OneToOneField(Subasta, on_delete=models.CASCADE)
    #Producto = models.OneToOneField(Producto, on_delete=models.CASCADE)