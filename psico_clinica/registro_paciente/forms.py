"""Formularios"""
from django import forms
from .models import Paciente

class PatientForm(forms.ModelForm):
    """Formulario para agregar un nuevo paciente"""
    class Meta:
        """Especificaciones"""
        model = Paciente

        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'id_sexo',
            'telefono_movil',
            'id_localidad',
            'id_congregacion',
            'id_estado_civil',
            'id_referencia',
        ]
        labels = {
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'fecha_nacimiento':'Fecha de nacimiento',
            'id_sexo':'Sexo',
            'telefono_movil':'Telefono movil',
            'id_localidad':'Localidad',
            'id_congregacion':'Congregacion',
            'id_estado_civil':'Estado civil',
            'id_referencia':'Referenciado por',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'Nombres',
                                            'name':'nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control',
                                              'type':'text',
                                              'placeholder':'Apellidos',
                                              'name':'apellido'}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control',
                                                      'type':'date',
                                                      'placeholder':'Fecha',
                                                      'name':'fecha_nacimiento'}),
            'id_sexo':forms.Select(attrs={'class':'custom-select',
                                          'name':'sexo'}),
            'telefono_movil':forms.TextInput(attrs={'type':'number',
                                                    'class':'form-control',
                                                    'name':'telefono_movil',
                                                    'placeholder':'########'}),
            'id_localidad':forms.Select(attrs={'class':'custom-select',
                                               'name':'localidad'}),
            'id_congregacion':forms.Select(attrs={'class':'custom-select',
                                                  'name':'congregacion'}),
            'id_estado_civil':forms.Select(attrs={'class':'custom-select',
                                                  'name':'estado_civil'}),
            'id_referencia':forms.Select(attrs={'class':'custom-select',
                                                'name':'referencia'}),
        }
