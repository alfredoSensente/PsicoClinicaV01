"""Pruebas al modelo paciente"""
import datetime
import factory

class LocalidadFactory(factory.django.DjangoModelFactory):
    """Factory de Localidad"""
    class Meta:
        model = 'registro_paciente.Localidad'

    municipio = 'Castillo'
    departamento = 'Narnia'
    direccion = 'Ropero'
    telefono_fijo = '24470279'

class EstadoCivilFactory(factory.django.DjangoModelFactory):
    """Factory de Estado Civil"""
    class Meta:
        model = 'registro_paciente.EstadoCivil'
    estado_civil = "Soltero/a"

class ReferenciaFactory(factory.django.DjangoModelFactory):
    """Factory de Referencia"""
    class Meta:
        model = 'registro_paciente.Referencia'
    referencia = "Docente"

class SexoFactory(factory.django.DjangoModelFactory):
    """Factory de Sexo"""
    class Meta:
        model = 'registro_paciente.Sexo'
    sexo = "Masculino"

class TipoReligionFactory(factory.django.DjangoModelFactory):
    """Factory de TipoReligion"""
    class Meta:
        model = 'registro_paciente.TipoReligion'
    nombre = "Catolica"

class CongregacionFactory(factory.django.DjangoModelFactory):
    """Factory de Congregacion"""
    class Meta:
        model = 'registro_paciente.Congregacion'
    nombre_congregacion = "Santa Lucia"
    congregacion_direccion = "Por ahí por ahí"
    id_tipo_religion = factory.SubFactory(TipoReligionFactory)

class PacienteFactory(factory.django.DjangoModelFactory):
    """Factory de Paciente"""
    class Meta:
        model = 'registro_paciente.Paciente'

    nombre = 'Giorno'
    apellido = 'Giovana'
    telefono_movil = '24470279'
    fecha_nacimiento = datetime.datetime.now().date()+datetime.timedelta(days=1)
    id_localidad = factory.SubFactory(LocalidadFactory)
    id_congregacion = factory.SubFactory(CongregacionFactory)
    id_estado_civil = factory.SubFactory(EstadoCivilFactory)
    id_referencia = factory.SubFactory(ReferenciaFactory)
    id_sexo = factory.SubFactory(SexoFactory)
