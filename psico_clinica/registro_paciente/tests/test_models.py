"""Pruebas de todos los modelos"""
import datetime
from django.test import TestCase
from dateutil.relativedelta import relativedelta
from .factories.pacientes import PacienteFactory

# Create your tests here.
class PacienteModelTests(TestCase):
    """pruebas para Modelo Paciente"""

    def test_paciente_menor_edad(self):
        """devuelve verdadero si la fecha de nacimiento es de hace menos de 18 anios"""
        paciente = PacienteFactory(fecha_nacimiento=datetime.datetime.now().date()
                                   - relativedelta(years=18, days=-1))
        self.assertIs(paciente.menor_edad(), True)


    def test_paciente_mayor_edad(self):
        """devuelve falso si la fecha de nacimiento es de hace mas de 18 anios"""
        paciente = PacienteFactory(fecha_nacimiento=datetime.datetime.now().date()
                                   - relativedelta(years=18, days=1))
        self.assertIs(paciente.menor_edad(), False)
