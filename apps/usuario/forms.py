from django import forms 
from .models import User

class ActualizarUsuarioForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'correo',
            'foto',
        ]

        widgets = {
            'correo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar la dirección de correo aquí.'}),
            'foto' : forms.FileInput(),
        }