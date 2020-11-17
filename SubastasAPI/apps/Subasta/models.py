from django.db import models

# Create your models here.
class Subasta(models.Model):
    """ Modelo para subastas"""
    NombreProducto = models.CharField(max_length=200)
    Estado = models.CharField(max_length=200, blank =True, default='')
    Precion_Final = models.FloatField()