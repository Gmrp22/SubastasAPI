from django.db import models
#from apps.Usuario.models import Usuario
from apps.Subasta.models import Subasta

class Producto(models.Model):
    """ Modelo del producto"""
    
    Nombre = models.CharField(max_length=200)
    Estado = models.CharField(max_length=200, default='Espera', blank =True)
    #Vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Subasta = models.ForeignKey(Subasta, on_delete=models.CASCADE, blank =True, null = True, default='')
