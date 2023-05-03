"""User URLS"""
from django.urls import path
from . import views

urlpatterns = [
    path('api-auth/', views.CustomObtainAuthToken.as_view()),
    path('patient-list/', views.PatientList.as_view()),
]
