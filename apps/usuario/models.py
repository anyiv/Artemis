from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Tipo_Usuario(models.Model):
    codigo = models.CharField(max_length=8, primary_key=True)
    tipo_usuario = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class User(AbstractUser):
    city = models.TextField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    type_u = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE, blank=True, null=True, default = 'cli')
    last_access = models.DateTimeField(default=timezone.now)    