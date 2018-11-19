from django import forms

from .models import Materia, Grado, Seccion

class GradoForm(forms.ModelForm):

    class Meta:
        model = Grado
        fields = [
            'nombre',
            'seccion',
            'materia',
        ]
        labels = {
            'nombre': 'Nombre',
            'seccion' : 'Seccion',
            'fecha': 'Fecha',
            'materia': 'Materia de grados',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'seccion': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.CheckboxSelectMultiple(),
        }
