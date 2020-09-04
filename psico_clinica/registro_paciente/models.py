"""modelos"""
import datetime
from dateutil.relativedelta import relativedelta
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
        db_table = 'localidad'

class TipoReligion(models.Model):
    """tipo_religion"""
    id_tipo_religion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_religion'

class EstadoCivil(models.Model):
    """estado civil"""
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=45)

    def __str__(self):
        return self.estado_civil

    class Meta:
        db_table = 'estado_civil'

class Referencia(models.Model):
    """referencia"""
    id_referencia = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=45)

    def __str__(self):
        return self.referencia

    class Meta:
        db_table = 'referencia'

class Carrera(models.Model):
    """carrera"""
    id_carrera = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=45)

    def __str__(self):
        return self.carrera

    class Meta:
        db_table = 'carrera'

class TipoFamiliar(models.Model):
    """tipo familiar"""
    id_tipo_familiar = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_tipo

    class Meta:
        db_table = 'tipo_familiar'

class Familiar(models.Model):
    """familiar"""
    id_familiar = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, db_column='id_paciente')
    id_tipo_familiar = models.ForeignKey('TipoFamiliar',
                                         on_delete=models.CASCADE, db_column='id_tipo_familiar')
    telefono_movil = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    trato_con_ellos = models.TextField(blank=True, null=True)
    vives_con_el = models.TextField(blank=True, null=True)
    direccion_trabajo = models.CharField(max_length=255, blank=True, null=True)
    ocupacion = models.CharField(max_length=45, blank=True, null=True)
    dui = models.CharField(max_length=45, blank=True, null=True)
    responsable = models.BooleanField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'familiar'
        unique_together = (('id_familiar', 'id_paciente', 'id_tipo_familiar'),)

class Congregacion(models.Model):
    """congregacion"""
    id_congregacion = models.AutoField(primary_key=True)
    nombre_congregacion = models.CharField(max_length=45)
    congregacion_direccion = models.CharField(max_length=255, blank=True, null=True)
    id_tipo_religion = models.ForeignKey('TipoReligion',
                                         on_delete=models.CASCADE, db_column='id_tipo_religion')

    def __str__(self):
        return self.nombre_congregacion

    class Meta:
        db_table = 'congregacion'
        unique_together = (('id_congregacion', 'id_tipo_religion'),)

class DatosClinicos(models.Model):
    """Datos Clincos"""
    id_datos_clinicos = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, db_column='id_paciente')
    nombre_enfermedad = models.CharField(max_length=45)
    medicamento = models.CharField(max_length=45)

    class Meta:
        db_table = 'datos_clinicos'
        unique_together = (('id_datos_clinicos', 'id_paciente'),)

class Sexo(models.Model):
    """Sexo"""
    id_sexo = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=45)

    def __str__(self):
        return self.sexo

    class Meta:
        db_table = 'sexo'

class Paciente(models.Model):
    """paciente"""
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    telefono_movil = models.CharField(max_length=45, blank=True, null=True)
    id_localidad = models.ForeignKey(Localidad, db_column='id_localidad', on_delete=models.CASCADE)
    id_congregacion = models.ForeignKey(Congregacion, on_delete=models.CASCADE,
                                        db_column='id_congregacion')
    id_estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE,
                                        db_column='id_estado_civil')
    id_referencia = models.ForeignKey('Referencia', on_delete=models.CASCADE,
                                      db_column='id_referencia')
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, db_column='id_sexo')

    def __str__(self):
        return self.nombre + " " + self.apellido

    def menor_edad(self):
        """Devuelve true si la fecha fue antes de hace 18 años"""
        return self.fecha_nacimiento >= datetime.datetime.now().date() - relativedelta(years=18)

    class Meta:
        db_table = 'paciente'
        unique_together = (('id_paciente', 'id_localidad', 'id_congregacion', 'id_estado_civil',
                            'id_referencia', 'id_sexo'),)

class Trabajo(models.Model):
    """trabajo"""
    id_trabajo = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_paciente')
    institucion = models.CharField(max_length=45)
    hace_cuanto_trabajas_ahí = models.CharField(max_length=45)
    cargo = models.CharField(max_length=45)

    class Meta:
        db_table = 'trabajo'
        unique_together = (('id_trabajo', 'id_paciente'),)

class TratamientoAnterior(models.Model):
    """Tratamiento Anterior"""
    id_tratamiento_anterior = models.IntegerField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_paciente')
    motivo = models.CharField(max_length=255)
    periodo = models.CharField(max_length=45, blank=True, null=True)
    dado_alta = models.BooleanField()
    alta_por_que_no = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tratamiento_anterior'
        unique_together = (('id_tratamiento_anterior', 'id_paciente'),)

class Educacion(models.Model):
    """Educacion del paciente en general"""
    id_educacion = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, db_column='id_paciente')

    def __str__(self):
        return str(self.id_educacion)

    class Meta:
        db_table = 'educacion'
        unique_together = (('id_educacion', 'id_paciente'),)

class EducacionBasica(models.Model):
    """Educacion baśica del paciente desde parvularia hasta 2do de bachillerato del paciente"""
    id_educacion_basica = models.AutoField(primary_key=True)
    id_educacion = models.ForeignKey(Educacion, on_delete=models.CASCADE, db_column='id_educacion')
    grado_escolar = models.CharField(max_length=45)
    institucion = models.CharField(max_length=45)

    def __str__(self):
        return self.institucion

    class Meta:
        db_table = 'educacion_basica'
        unique_together = (('id_educacion_basica', 'id_educacion'),)

class EducacionSuperior(models.Model):
    """Educacion superior del paciente"""
    id_educacion_superior = models.AutoField(primary_key=True)
    id_educacion = models.ForeignKey(Educacion, on_delete=models.CASCADE, db_column='id_educacion')
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, db_column='id_carrera')
    carnet = models.CharField(max_length=45)
    ciclo = models.CharField(max_length=45)
    universidad = models.CharField(max_length=45)
    finalizada = models.BooleanField()

    def __str__(self):
        return self.universidad

    class Meta:
        db_table = 'educacion_superior'
        unique_together = (('id_educacion_superior', 'id_educacion', 'id_carrera'),)

class Grado(models.Model):
    """Doctorados, master, grados, etc"""
    id_grado = models.AutoField(primary_key=True)
    id_educacion = models.ForeignKey(Educacion, on_delete=models.CASCADE, db_column='id_educacion')
    nombre_grado = models.CharField(max_length=45)
    finalizado = models.BooleanField()
    institucion = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_grado

    class Meta:
        db_table = 'grado'
        unique_together = (('id_grado', 'id_educacion'),)
