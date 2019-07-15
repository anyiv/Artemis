from django.contrib import admin
from apps.usuario.models import Tipo_Usuario, User

# Register your models here.
admin.site.register(Tipo_Usuario)
admin.site.register(User)