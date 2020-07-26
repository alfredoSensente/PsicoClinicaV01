"""modelos"""
from django.db import models

# Create your models here.
class Localidad(models.Model):
    """localidad"""
    id_localidad = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.direccion

    class Meta:
        managed = False
        db_table = 'localidad'

class TipoReligion(models.Model):
    """tipo_religion"""
    id_tipo_religion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tipo_religion'
