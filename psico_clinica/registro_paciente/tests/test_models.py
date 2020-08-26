"""Pruebas de todos los modelos"""
from django.test import TestCase
from .factories.pacientes import PacienteFactory
from dateutil.relativedelta import relativedelta
import datetime

# Create your tests here.
class PacienteModelTests(TestCase):
    """pruebas para Modelo Paciente"""

    def test_paciente_nacido_en_futuro(self):
        """Regresa falso si la fecha de nacimiento esta en futuro"""
        paciente = PacienteFactory()
        self.assertIs(paciente.fecha_valida(), False)

    def test_paciente_menor_edad(self):
        """devuelve falso si la fecha de nacimiento es de hace mas de 18 anios"""
        paciente = PacienteFactory(fecha_nacimiento=datetime.datetime.now().date()
                                   - relativedelta(years=19))
        self.assertIs(paciente.menor_edad(), False)
