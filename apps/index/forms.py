from django import forms 
from apps.usuario.models import User
from django.contrib.auth.forms import PasswordChangeForm

class Cambiarcontrasena(PasswordChangeForm):

    class Meta:
        model = User

        fields = [
            'new_password1',
            'new_password2',
        ]


