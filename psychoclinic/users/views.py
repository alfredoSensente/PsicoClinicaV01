"""User Views"""
from .authentication import AuthListAPIView
from .models import Patient
from .serializers import PatientSerializer

class PatientList(AuthListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
