"""vistas"""
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Paciente, Localidad, Congregacion, Referencia, EstadoCivil

# Create your views here.
class IndexView(generic.ListView):
    """Vista Generica ListView"""
    model = Paciente
    context_object_name = 'latest_patient_list'
    template_name = 'registro_paciente/index.html'
    def get_queryset(self):
        return Paciente.objects.all()[:10]

class PatientDetailView(generic.DetailView):
    """Vista generica detalle_paciente"""
    model = Paciente
    context_object_name = 'paciente_seleccionado'
    template_name = 'registro_paciente/detalle_paciente.html'

def nuevo_paciente(request):
    """Registra un nuevo paciente"""
    lista_localidad = Localidad.objects.all()
    lista_congregacion = Congregacion.objects.all()
    lista_estado_civil = EstadoCivil.objects.all()
    lista_referencia = Referencia.objects.all()
    context = {
        'lista_localidad' : lista_localidad,
        'lista_congregacion' : lista_congregacion,
        'lista_estado_civil' : lista_estado_civil,
        'lista_referencia' : lista_referencia,
    }
    return render(request, 'registro_paciente/nuevo_paciente.html', context)

def agregar(request):
    """Agregar"""
    try:
        referencia_seleccionada = get_object_or_404(Referencia,
                                                    id_referencia=request.POST['referencia'])
        localidad_seleccionada = get_object_or_404(Localidad,
                                                   id_localidad=request.POST['localidad'])
        e_civil_seleccionada = get_object_or_404(EstadoCivil,
                                                 id_estado_civil=request.POST['estado_civil'])
        congregacion_seleccionada = get_object_or_404(Congregacion,
                                                      id_congregacion=request.POST['congregacion'])
    except (KeyError, Referencia.DoesNotExist, Localidad.DoesNotExist, EstadoCivil.DoesNotExist,
            Congregacion.DoesNotExist):
        context_error = {
            'error_message': "Error: No has llenado un campo obligatorio.",
        }
        return render(request, 'registro_paciente/nuevo_paciente.html', context_error)
    else:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono_movil = request.POST['telefono_movil']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        sexo = request.POST['sexo']

        nuevo_paciente = Paciente(nombre=nombre,
                                  apellido=apellido,
                                  fecha_nacimiento=fecha_nacimiento,
                                  sexo=sexo,
                                  telefono_movil=telefono_movil,
                                  id_localidad=localidad_seleccionada,
                                  id_congregacion=congregacion_seleccionada,
                                  id_estado_civil=e_civil_seleccionada,
                                  id_referencia=referencia_seleccionada)
        nuevo_paciente.save()
        return HttpResponseRedirect(reverse('registro_paciente:index'))
