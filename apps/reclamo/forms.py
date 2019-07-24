from django import forms 
from .models import Categoria

class IncluirCategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'nombre',
            'descripcion',
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
        }