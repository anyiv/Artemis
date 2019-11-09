from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.datos_externos.models import Empleado, Cliente
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

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
    idEmpleado = models.OneToOneField(Empleado,on_delete=models.CASCADE, default=None, blank=True, null=True)  
    idCliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, default=None, blank=True, null=True)
    codTipoUser = models.ForeignKey(TipoUser, on_delete=models.CASCADE, blank=True, null=True, default = 'cli')
    correo = models.EmailField(max_length=30,unique=True)
    foto = models.ImageField(upload_to='usuarios/fotos/', default='usuarios/fotos/default.jpg')
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')
    USERNAME_FIELD = 'nombreUsuario'
    EMAIL_FIELD = 'correo'
    REQUIRED_FIELDS = ['correo','idEmpleado']

    objects = UserManager()

    def enviarCorreo(self, asunto, linea1, linea2="", linea3=""):
        nombre = self.idCliente.nombre + " " + self.idCliente.apellido
        contenido = render_to_string('correo_base.html',{'linea1':linea1,'linea2':linea2,'linea3':linea3,'nombre':nombre})
        send_mail('Artemis - ' + asunto,strip_tags(contenido),'admin@artemis.com',{self.correo},html_message=contenido)

    def login_grec(self):
        if self.last_login:
            last_login = self.last_login.date()
            hoy = timezone.now().date()
            if last_login != hoy:
                eg = EficienciaGestor.objects.get(nombreUsuario = self)
                eg.diasActivo += 1
                eg.save()
                self.actualizar_eficiencia()
        else:
            eg = EficienciaGestor.objects.get(nombreUsuario = self)
            eg.diasActivo += 1
            eg.save()
            self.actualizar_eficiencia()

    def actualizar_rec_atendidos(self):
        print("TBD")

    def actualizar_eficiencia(self):
        eg = EficienciaGestor.objects.get(nombreUsuario = self)
        eg.eficiencia = eg.recAtendidos / eg.diasActivo
        eg.save()

class EficienciaGestor(models.Model):
    nombreUsuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    diasActivo = models.IntegerField(default=0)
    recAtendidos = models.IntegerField(default=0)
    eficiencia = models.FloatField(default=0)

@receiver(post_save, sender=User)
def crear_eficiciencia(sender, instance, **kwargs):
    try:
        EficienciaGestor.objects.get(nombreUsuario = instance.nombreUsuario)
    except:
        if instance.codTipoUser.codTipoUser == "grec":
            eg = EficienciaGestor()
            eg.nombreUsuario = instance
            eg.save()