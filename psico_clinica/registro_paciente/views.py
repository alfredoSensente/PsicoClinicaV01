"""vistas"""
from django.shortcuts import render, get_object_or_404
from .models import Paciente, Localidad, Congregacion, Referencia, EstadoCivil

# Create your views here.
def index(request):
    """prueba"""
    latest_patient_list = Paciente.objects.all()[:5]
    context = {
        'latest_patient_list' : latest_patient_list,
    }
    return render(request, 'registro_paciente/index.html', context)

def detalle_paciente(request, id_paciente):
    """detale_carrera"""
    paciente_seleccionado = get_object_or_404(Paciente, id_paciente=id_paciente)
    context = {
        'paciente_seleccionado' : paciente_seleccionado,
    }
    return render(request, 'registro_paciente/detalle_paciente.html', context)

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
