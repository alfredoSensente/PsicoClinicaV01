"""vistas"""
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Paciente
from .forms import PacienteForm

# Create your views here.
class IndexView(generic.ListView):
    """Vista Generica ListView"""
    paginate_by = 5
    model = Paciente
    context_object_name = 'latest_patient_list'
    template_name = 'registro_paciente/index.html'
    def get_queryset(self):
        return Paciente.objects.all()


class PatientDetailView(generic.DetailView):
    """Vista generica detalle_paciente"""
    model = Paciente
    context_object_name = 'paciente_seleccionado'
    template_name = 'registro_paciente/detalle_paciente.html'


class PacienteCreate(generic.CreateView):
    """Crear un nuevo paciente"""
    model = Paciente
    form_class = PacienteForm
    template_name = 'registro_paciente/nuevo_paciente.html'
    success_url = reverse_lazy('registro_paciente:index')

    def post(self, request, *args, **kwargs):
        form = PacienteForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('registro_paciente:index'))
        else:
            return render(request, 'registro_paciente/nuevo_paciente.html',
                          {'form': form, 'error_date': 'Debes introducir una fecha valida'})


class PacienteUpdate(generic.UpdateView):
    """Actualiza el registro de un paciente"""
    model = Paciente
    form_class = PacienteForm
    template_name = 'registro_paciente/nuevo_paciente.html'
    success_url = reverse_lazy('registro_paciente:index')


class PacienteDelete(generic.DeleteView):
    """Borra un paciente"""
    model = Paciente
    context_object_name = 'paciente_seleccionado'
    template_name = 'registro_paciente/borrar_paciente.html'
    success_url = reverse_lazy('registro_paciente:index')
