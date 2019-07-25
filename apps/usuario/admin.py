from django.contrib import admin
from apps.usuario.models import TipoUser, User

# Register your models here.
admin.site.register(TipoUser)
admin.site.register(User)