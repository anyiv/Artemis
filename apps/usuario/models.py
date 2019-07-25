from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.datos_externos.models import Empleado, Cliente, Persona

# Create your models here.
class TipoUser(models.Model):
    codTipoUser = models.CharField(max_length=8, primary_key=True)
    tipoUser = models.CharField(max_length=10)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

    def __str__(self):
        return self.tipoUser

class UserManager(BaseUserManager):
    def create_user(self, nombreUsuario, identificacion, correo, codTipoUser=None, estatus='A', password = None):
        user_obj = self.model(
            correo=self.normalize_email(correo)
        )
        user_obj.set_password(password)
        user_obj.nombreUsuario = nombreUsuario
        user_obj.codTipoUser = TipoUser.objects.get(codTipoUser='cli')
        user_obj.identificacion = Persona.objects.get(identificacion='1')
        user_obj.correo = correo
        user_obj.estatus = estatus
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, nombreUsuario, identificacion, correo, codTipoUser=None, estatus='A', password=None):
        user = self.create_user(
            nombreUsuario,
            Persona.objects.get(identificacion='1'),
            correo,
            TipoUser.objects.get(codTipoUser='admin'),
            estatus,
            password=password,
        )
        return user

class User(AbstractBaseUser):
    nombreUsuario = models.CharField(max_length=20, primary_key=True, unique=True)
    codTipoUser = models.ForeignKey(TipoUser, on_delete=models.CASCADE, blank=True, null=True, default = 'cli')
    identificacion = models.ForeignKey(Persona,on_delete=models.CASCADE)  
    correo = models.EmailField(max_length=30)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')
    USERNAME_FIELD = 'nombreUsuario'
    EMAIL_FIELD = 'correo'
    REQUIRED_FIELDS = ['correo','identificacion']

    objects = UserManager()