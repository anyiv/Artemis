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
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8}),
        }

class ConsultarCategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'codCategoria',
            'nombre',
            'descripcion',
            'estatus',
        ]

        widgets = {
            'codCategoria' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'nombre' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'readonly':''}),
            'estatus' : forms.TextInput(attrs={'class':'form-control','id':'estatus','type':'hidden'}),
        }

class ActualizarCategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'codCategoria',
            'nombre',
            'descripcion',
        ]

        widgets = {
            'codCategoria' : forms.TextInput(attrs={'class':'form-control', 'readonly':''}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8}),
        }