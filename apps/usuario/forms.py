from django import forms 
from .models import User
from django.contrib.auth.forms import UserCreationForm

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

class CrearUsuario(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'idEmpleado',
            'nombreUsuario',
            'password1',
            'correo',
            'codTipoUser',
            'idCliente',
        ]

        widgets = {
            'idEmpleado' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa la identificación aquí.'}),
            'nombreUsuario' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa el nombre de usuario aquí.'}),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),
            'correo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa la dirección de correo aquí.'}),
            'codTipoUser' : forms.Select(attrs={'class':'form-control'}),
            'idCliente' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa la identificación aquí.'})
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
