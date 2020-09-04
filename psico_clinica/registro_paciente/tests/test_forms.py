"""Pruebas para formularios"""
from django.test import TestCase
from registro_paciente.forms import PacienteForm
from .factories.pacientes import PacienteFactory

# Create your tests here.
class PacienteFormTests(TestCase):
    """Prueba del formulario PacienteForm"""

    def test_fecha_del_futuro(self):
        """Devuelve una True si la fecha es hoy o esta en el pasado"""
        form = PacienteForm(data={'fecha_nacimiento':PacienteFactory.fecha_nacimiento})
        self.assertEqual(form.errors["fecha_nacimiento"], ["La fecha no debe estar en el futuro"])
