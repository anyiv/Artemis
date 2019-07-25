from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.datos_externos.models import Empleado, Cliente
from django.contrib.auth.models import PermissionsMixin

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
    def create_user(self, nombreUsuario, idCliente, idEmpleado, correo, is_staff=False, is_superuser=False, codTipoUser='cli', estatus='A', password = None):
        user_obj = self.model(
            correo=self.normalize_email(correo)
        )
        user_obj.set_password(password)
        user_obj.nombreUsuario = nombreUsuario
        user_obj.idCliente = Cliente.objects.get(identificacion=idCliente)
        user_obj.idEmpleado = Empleado.objects.get(identificacion=idEmpleado)
        user_obj.codTipoUser = TipoUser.objects.get(codTipoUser=codTipoUser)
        user_obj.correo = correo
        user_obj.estatus = estatus
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, nombreUsuario, correo, idEmpleado, idCliente = '0', is_staff=True, is_superuser=True, codTipoUser='admin', estatus='A', password=None):
        user = self.create_user(
            nombreUsuario,
            idCliente,
            idEmpleado,
            correo,
            is_staff,
            is_superuser,
            codTipoUser,
            estatus,
            password=password,
        )
        return user

class User(AbstractBaseUser,PermissionsMixin):
    nombreUsuario = models.CharField(max_length=20, primary_key=True, unique=True)
    idEmpleado = models.ForeignKey(Empleado,on_delete=models.CASCADE, unique=True, default=None, blank=True, null=True)  
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, unique=True, default=None, blank=True, null=True)
    codTipoUser = models.ForeignKey(TipoUser, on_delete=models.CASCADE, blank=True, null=True, default = 'cli')
    correo = models.EmailField(max_length=30,unique=True)
    foto = models.ImageField(upload_to='usuarios/fotos/', default='usuarios/fotos/default.jpg')
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')
    USERNAME_FIELD = 'nombreUsuario'
    EMAIL_FIELD = 'correo'
    REQUIRED_FIELDS = ['correo','idEmpleado']

    objects = UserManager()