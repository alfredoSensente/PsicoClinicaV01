"""modelos"""
from django.db import models

# Create your models here.
class Localidad(models.Model):
    """Localidad"""
    id_localidad = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    direccion = models.CharField(max_length=150)
    telefono_fijo = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        """muestra el nombre del municipio"""
        return self.telefono_fijo

    class Meta:
        managed = False
        db_table = 'localidad'
