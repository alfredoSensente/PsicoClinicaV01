"""urls de registro paciente"""
from django.urls import path

from . import views

app_name='registro_paciente'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_paciente>/', views.detalle_paciente, name='detalle_paciente'),
]
