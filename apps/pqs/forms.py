from django import forms 
from .models import PQS

class CrearPeticion(forms.ModelForm):

    class Meta:
        model = PQS

        fields = [
            'categoria',
            'nombreUsuario',
            'descripcion',
        ]

        widgets = {
            'categoria' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'placeholder':'Por favor ingrese su petición aquí...','required':''}),
            'nombreUsuario' : forms.TextInput(attrs={'id':'nombreusuario', 'type':'hidden'}),
        }

class CrearQueja(forms.ModelForm):

    class Meta:
        model = PQS

        fields = [
            'categoria',
            'nombreUsuario',
            'descripcion',
        ]

        widgets = {
            'categoria' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'placeholder':'Por favor ingrese su queja aquí...'}),
            'nombreUsuario' : forms.TextInput(attrs={'type':'hidden','id':'nombreusuario'}),
        }

class CrearSugerencia(forms.ModelForm):

    class Meta:
        model = PQS

        fields = [
            'categoria',
            'nombreUsuario',
            'descripcion',
        ]

        widgets = {
            'categoria' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'placeholder':'Por favor ingrese su sugerencia aquí...'}),
            'nombreUsuario' : forms.TextInput(attrs={'type':'hidden','id':'nombreusuario'}),
        }

class AtenderPQS(forms.ModelForm):

    class Meta:
        model = PQS

        fields = [
            'estatus',
        ]

        widgets = {
            'estatus' : forms.TextInput(attrs={'class':'form-control'}),
        }