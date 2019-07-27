from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Oficina)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Zona)
admin.site.register(Contrato)
admin.site.register(Servicio)
admin.site.register(DetalleContrato)