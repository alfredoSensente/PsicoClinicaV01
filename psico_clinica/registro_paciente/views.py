"""vistas"""
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Paciente
from .forms import PatientForm

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

class PacienteCreate(generic.CreateView):
    """Crear un nuevo paciente"""
    model = Paciente
    form_class = PatientForm
    template_name = 'registro_paciente/nuevo_paciente.html'
    success_url = reverse_lazy('registro_paciente:index')

class PacienteUpdate(generic.UpdateView):
    """Actualiza el registro de un paciente"""
    model = Paciente
    form_class = PatientForm
    template_name = 'registro_paciente/nuevo_paciente.html'
    success_url = reverse_lazy('registro_paciente:index')

class PacienteDelete(generic.DeleteView):
    """Borra un paciente"""
    model = Paciente
    context_object_name = 'paciente_seleccionado'
    template_name = 'registro_paciente/borrar_paciente.html'
    success_url = reverse_lazy('registro_paciente:index')
