#from django.shortcuts import render
"""vistas"""
from django.http import HttpResponse

# Create your views here.
def index(request):
    """prueba"""
    return HttpResponse("hola mundo")
