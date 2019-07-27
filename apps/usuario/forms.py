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

class CrearUsuario(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'idEmpleado',
            'nombreUsuario',
            'password',
            'correo',
            'codTipoUser',
        ]

        widgets = {
            'idEmpleado' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar la identificación aquí.'}),
            'nombreUsuario' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar el nombre de usuario aquí.'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar lacontraseña aquí.'}),
            'correo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar la dirección de correo aquí.'}),
            'codTipoUser' : forms.Select(attrs={'class':'form-control'}),
        }  

class ConsultarEmpleado(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'nombreUsuario',
            'correo',
            'estatus',
        ]

        widgets = {
            'nombreUsuario' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'correo' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'estatus' : forms.TextInput(attrs={'class':'form-control','id':'estatus','type':'hidden'}),
        }   

class ConsultarCliente(forms.ModelForm):

    class Meta:
        model = User   

        fields = [
            'nombreUsuario',
            'correo',
            'estatus',
        ]

        widgets = {
            'nombreUsuario' : forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'correo': forms.TextInput(attrs={'class':'form-control','readonly':''}),
            'estatus' : forms.TextInput(attrs={'class':'form-control','id':'estatus','type':'hidden'}),
        }
