"""urls de registro paciente"""
from django.urls import path

from . import views

app_name='registro_paciente'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='detalle_paciente'),
    path('nuevo_paciente/', views.PacienteCreate.as_view(), name='nuevo_paciente'),
    path('editar_paciente/<int:pk>/', views.PacienteUpdate.as_view(), name='editar_paciente'),
]
