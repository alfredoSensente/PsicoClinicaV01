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

class EstadoCivil(models.Model):
    """estado civil"""
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=45)

    def __str__(self):
        return self.estado_civil

    class Meta:
        managed = False
        db_table = 'estado_civil'

class Referencia(models.Model):
    """referencia"""
    id_referencia = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=45)

    def __str__(self):
        return self.referencia

    class Meta:
        managed = False
        db_table = 'referencia'

class Carrera(models.Model):
    """carrera"""
    id_carrera = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=45)

    def __str__(self):
        return self.carrera

    class Meta:
        managed = False
        db_table = 'carrera'

class TipoFamiliar(models.Model):
    """tipo familiar"""
    id_tipo_familiar = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_tipo

    class Meta:
        managed = False
        db_table = 'tipo_familiar'
