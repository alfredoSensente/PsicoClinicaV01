"""vistas"""
from django.shortcuts import render, get_object_or_404
from .models import Paciente

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
    paciente_seleccionado = Paciente.objects.filter(id_paciente=id_paciente)
    context = {
        'paciente_seleccionado' : paciente_seleccionado,
    }
    return render(request, 'registro_paciente/detalle_paciente.html', context)
