"""User Views"""
from .authentication import AuthListAPIView
from .models import Patient, Doctor
from .serializers import PatientSerializer

class PatientList(AuthListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class DoctorList(AuthListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = PatientSerializer
