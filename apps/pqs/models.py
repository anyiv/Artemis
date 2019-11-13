from django.db import models
from apps.usuario.models import User
from datetime import datetime
from notifications.signals import notify

# Create your models here.
class PQS(models.Model):

    def cod_pqs():
        pqs = PQS
        ult_pqs = pqs.objects.all().count()

        if not ult_pqs:
            return 'PQS-0000'

        nro_pqs = int(ult_pqs)
        nvo_codpqs = 'PQS-' + str(nro_pqs).zfill(4) 

        return nvo_codpqs

    codPQS = models.CharField(max_length=8,default=cod_pqs, primary_key=True)
    nombreUsuario = models.ForeignKey(User, related_name='creador', on_delete=models.CASCADE, blank=False, null=False)
    CATEGORIA = (
        ('P','Peticion'),
        ('Q','Queja'),
        ('S','Sugerencia'),
    )
    categoria = models.CharField(max_length=1,choices=CATEGORIA, blank=False, null=False)
    descripcion = models.CharField(max_length=500)
    fechaRegistro = models.DateTimeField(default=datetime.now)
    fechaFinalizado = models.DateTimeField(blank=True ,null=True)
    responsablePQS = models.ManyToManyField(User, related_name='responsable', blank=True)
    ESTATUS = ( 
        ('P','Pendiente'),
        ('M','Marcada'),
        ('A','Atendida'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='P')

    def __str__(self):
        return self.codPQS + ' / ' + self.nombreUsuario.nombreUsuario +' / ' + self.nombreUsuario.idCliente.nombre + ' / ' + self.descripcion[:20] + '...'

class HistoricoPQS(models.Model):
    pqs = models.ForeignKey(PQS, on_delete=models.CASCADE,blank=True, null=True)
    fecha = models.DateField(auto_now = True, blank=True, null=True)
    detalle = models.CharField(max_length = 200)
    usuarioEncargado = models.CharField(max_length = 20)

    def notificar(self, descripcion):
        notify.send(sender=self, recipient=self.pqs.nombreUsuario, verb='n', description=descripcion)

    def __str__(self):
        return self.pqs.codPQS