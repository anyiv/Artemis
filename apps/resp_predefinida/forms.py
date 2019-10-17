from django import forms 
from .models import RespuestaPredefinida


class IncluirRespuestaP(forms.ModelForm):

    class Meta:
        model = RespuestaPredefinida

        fields = [
            'categoria',
            'descripcion'
        ]

        widgets = {
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'placeholder':'Ingresar descripción de la respuesta predefinidas aquí.'}),
        }

class ConsultarRespuestaP(forms.ModelForm):
    
    class Meta:
        model = RespuestaPredefinida

        fields = [
            'codRespuestaP',
            'categoria',
            'contUso',
            'descripcion',
            'estatus',
        ]

        widgets = {
            'codRespuestaP' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'categoria' : forms.Select(attrs={'class':'form-control','disabled':''}),
            'contUso' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8,'readonly':''}),
            'estatus' : forms.TextInput(attrs={'class':'form-control','id':'estatus','type':'hidden'}),
        }

class ModificarRespuestaP(forms.ModelForm):

    class Meta:
        model = RespuestaPredefinida

        fields = [
             'codRespuestaP',
            'categoria',
            'descripcion',
            'estatus'
        ]

        widgets = {
            'codRespuestaP' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','cols':6,'rows':8}),
            'estatus' : forms.TextInput(attrs={'class':'form-control','id':'estatus','type':'hidden'}),
        }