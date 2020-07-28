"""modelos"""
from django.db import models

# Create your models here.
class Localidad(models.Model):
    """localidad"""
    id_localidad = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    direccion = models.CharField(max_length=255)
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

class Familiar(models.Model):
    """familiar"""
    id_familiar = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    id_tipo_familiar = models.ForeignKey('TipoFamiliar',
                                         models.DO_NOTHING, db_column='id_tipo_familiar')
    telefono_movil = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    trato_con_ellos = models.TextField(blank=True, null=True)
    vives_con_el = models.TextField(blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=255, blank=True, null=True)
    ocupacion = models.CharField(max_length=45, blank=True, null=True)
    dui = models.CharField(max_length=45, blank=True, null=True)
    responsable = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'familiar'
        unique_together = (('id_familiar', 'id_paciente', 'id_tipo_familiar'),)

class Congregacion(models.Model):
    """congregacion"""
    id_congregacion = models.AutoField(primary_key=True)
    nombre_congregacion = models.CharField(max_length=45)
    congregacion_direccion = models.CharField(max_length=255, blank=True, null=True)
    id_tipo_religion = models.ForeignKey('TipoReligion',
                                         models.DO_NOTHING, db_column='id_tipo_religion')

    def __str__(self):
        return self.nombre_congregacion

    class Meta:
        managed = False
        db_table = 'congregacion'
        unique_together = (('id_congregacion', 'id_tipo_religion'),)

class DatosClinicos(models.Model):
    """Datos Clincos"""
    id_datos_clinicos = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    nombre_enfermedad = models.CharField(max_length=45)
    medicamento = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'datos_clinicos'
        unique_together = (('id_datos_clinicos', 'id_paciente'),)

class Paciente(models.Model):
    """paciente"""
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=45)
    telefono_movil = models.CharField(max_length=45, blank=True, null=True)
    id_localidad = models.ForeignKey(Localidad, models.DO_NOTHING, db_column='id_localidad')
    id_congregacion = models.ForeignKey(Congregacion, models.DO_NOTHING,
                                        db_column='id_congregacion')
    id_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_estado_civil')
    id_referencia = models.ForeignKey('Referencia', models.DO_NOTHING, db_column='id_referencia')

    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        managed = False
        db_table = 'paciente'
        unique_together = (('id_paciente', 'id_localidad', 'id_congregacion', 'id_estado_civil',
                            'id_referencia'),)

class Trabajo(models.Model):
    """trabajo"""
    id_trabajo = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente')
    institucion = models.CharField(max_length=45)
    hace_cuanto_trabajas_ahí = models.CharField(max_length=45)
    cargo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'trabajo'
        unique_together = (('id_trabajo', 'id_paciente'),)

class TratamientoAnterior(models.Model):
    """Tratamiento Anterior"""
    id_tratamiento_anterior = models.IntegerField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente')
    motivo = models.CharField(max_length=255)
    periodo = models.CharField(max_length=45, blank=True, null=True)
    dado_alta = models.IntegerField()
    alta_por_que_no = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento_anterior'
        unique_together = (('id_tratamiento_anterior', 'id_paciente'),)
