"""Registra todos los modelos en admin"""
from django.contrib import admin
from .models import Localidad
from .models import TipoReligion
from .models import TipoFamiliar
from .models import Carrera
from .models import Referencia
from .models import EstadoCivil
from .models import Familiar
from .models import Congregacion
from .models import DatosClinicos
from .models import Paciente
from .models import Trabajo
from .models import TratamientoAnterior
from .models import Educacion
from .models import EducacionBasica
from .models import EducacionSuperior
from .models import Grado

# Register your models here.
admin.site.register(Localidad)
admin.site.register(TipoFamiliar)
admin.site.register(TipoReligion)
admin.site.register(Carrera)
admin.site.register(Referencia)
admin.site.register(EstadoCivil)
admin.site.register(Familiar)
admin.site.register(Congregacion)
admin.site.register(DatosClinicos)
admin.site.register(Paciente)
admin.site.register(Trabajo)
admin.site.register(TratamientoAnterior)
admin.site.register(Educacion)
admin.site.register(EducacionBasica)
admin.site.register(EducacionSuperior)
admin.site.register(Grado)
