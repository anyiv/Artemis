from django import forms 
from .models import Categoria, Reclamo

class IncluirCategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'nombre',
            'descripcion',
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar nombre de categoría aquí.'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'placeholder':'Ingresar descripción de categoría aquí.'}),
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

class IncluirReclamo(forms.ModelForm):

    class Meta:
        model = Reclamo

        fields = [
            'nombreUsuario',
            'descripcion',
            'codDetContrato',
            'codCategoria',
        ]

        widgets = {
            'nombreUsuario' : forms.TextInput(attrs={'id':'nombreusuario', 'type':'hidden'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':12,'placeholder':'Por favor escriba su reclamo aquí...'}),
        }

class ConsultarReclamo(forms.ModelForm):
    
    class Meta:
        model = Reclamo

        fields = [
            'estatus',
        ]
        
        widgets = {
            'estatus' :  forms.TextInput(attrs={'class':'form-control','readonly':''}),
        }

class AtenderReclamo(forms.ModelForm):

    class Meta:
        model = Reclamo

        fields = [
            'fechaEstimada',
            'codCategoria',
            'estatus',
            'fechaFinalizada',
        ]

        widgets = {
            'fechaEstimada' : forms.DateInput(attrs={'class':'form-control'}),
            'estatus' : forms.Select(attrs={'class':'form-control','id':'estatus'}),
            'codCategoria' : forms.Select(attrs={'class':'form-control'}),
            'fechaFinalizada' : forms.DateTimeInput(attrs={'class':'form-control'}),
        }
