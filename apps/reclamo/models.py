from django.db import models
from datetime import datetime, timedelta
from apps.datos_externos.models import DetalleContrato
from apps.usuario.models import User
from apps.usuario.models import EficienciaGestor
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Categoria(models.Model):

    def cod_categoria():
        categoria = Categoria
        ult_categoria = categoria.objects.all().count()

        if not ult_categoria:
            return 'CTR-0000'

        nro_categoria = int(ult_categoria)
        nvo_codcategoria = 'CTR-' + str(nro_categoria).zfill(4) 

        return nvo_codcategoria

    codCategoria = models.CharField(max_length=8, default=cod_categoria, primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

    def __str__(self):
        return self.nombre

class Reclamo(models.Model):

    def cod_reclamo():
        reclamo = Reclamo
        ult_reclamo = reclamo.objects.all().count()

        if not ult_reclamo:
            return 'REC-0000'

        nro_reclamo = int(ult_reclamo)
        nvo_codreclamo = 'REC-' + str(nro_reclamo).zfill(4) 

        return nvo_codreclamo

    codReclamo = models.CharField(max_length=8, default=cod_reclamo, primary_key=True)
    codDetContrato = models.ForeignKey(DetalleContrato, on_delete=models.CASCADE)
    codCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,blank=True, null=True)
    nombreUsuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='autor')
    descripcion = models.CharField(max_length=500)
    fechaRegistro = models.DateTimeField(default=datetime.now)
    fechaEstimada = models.DateField(blank=True, null=True)
    fechaFinalizada = models.DateTimeField(blank=True, null=True)
    responsableReclamo = models.ManyToManyField(User, blank=True)
    valoracion = models.CharField(max_length=1,blank=True, null=True)
    ESTATUS = ( 
        ('P','Pendiente'),
        ('R','En proceso'),
        ('F','Finalizado'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='P')

    def __str__(self):
        return self.codReclamo + ' / ' + self.nombreUsuario.nombreUsuario +' / ' + self.nombreUsuario.idCliente.nombre + ' / ' + self.descripcion[:20] + '...'

class HistoricoReclamo(models.Model):
    reclamo = models.ForeignKey(Reclamo, on_delete=models.CASCADE,blank=True, null=True)
    fecha = models.DateField(auto_now = True, blank=True, null=True)
    detalle = models.CharField(max_length = 200)
    TIPO = (
        ('A','Actualizacion'),
        ('C','Comentario'),
    )
    tipo = models.CharField(max_length=1,choices=TIPO, default='A')
    usuarioEncargado = models.CharField(max_length = 20)

class Configuracion(models.Model):
    nombre = models.CharField(max_length=10)
    valor = models.IntegerField()

@receiver(post_save, sender=Reclamo)
def asignar_reclamo(sender, instance, **kwargs):
    if instance.responsableReclamo.all().count() == 0:
        minimo = Configuracion.objects.get(id=1).valor
        maximo = Configuracion.objects.get(id=2).valor
        gestores = User.objects.filter(codTipoUser = "grec", estatus = "A", is_active = True)
        gestores_posibles = list()
        gestores_max = list() 
        correspondencia = list()
        correspondencia_max = list()

        for gestor in gestores:
            eg = EficienciaGestor.objects.get(nombreUsuario = gestor)
            cantidad = Reclamo.objects.filter(responsableReclamo=gestor).exclude(estatus="F").count()
            
            if cantidad < minimo:
                instance.responsableReclamo.add(gestor)
                dias_tarda = round((cantidad / eg.eficiencia) + 0.5) + 1
                hoy = datetime.now()
                while dias_tarda > 0:
                    hoy += timedelta(days=1)
                    dia_semana = hoy.weekday()
                    if dia_semana >= 5:
                        continue
                    dias_tarda -= 1
                instance.fechaEstimada = hoy
                instance.save()
                return
            elif cantidad < maximo:
                gestores_posibles.append(gestor)
                correspondencia.append(cantidad / eg.eficiencia)
            else:
                gestores_max.append(gestor)
                correspondencia_max.append(cantidad / eg.eficiencia)

        if len(correspondencia) != 0:
            indice = correspondencia.index(min(correspondencia))
            instance.responsableReclamo.add(gestores_posibles[indice])
            cantidad = Reclamo.objects.filter(responsableReclamo=gestores_posibles[indice]).exclude(estatus="F").count()
            eg = EficienciaGestor.objects.get(nombreUsuario=gestores_posibles[indice])
            dias_tarda = round((cantidad / eg.eficiencia) + 0.5) + 2
            hoy = datetime.now()
            while dias_tarda > 0:
                hoy += timedelta(days=1)
                dia_semana = hoy.weekday()
                if dia_semana >= 5:
                    continue
                dias_tarda -= 1
            instance.fechaEstimada = hoy
            instance.save()
        elif len(correspondencia_max) != 0:
            indice = correspondencia_max.index(min(correspondencia_max))
            instance.responsableReclamo.add(gestores_max[indice])
            cantidad = Reclamo.objects.filter(responsableReclamo=gestores_max[indice]).exclude(estatus="F").count()
            eg = EficienciaGestor.objects.get(nombreUsuario=gestores_max[indice])
            dias_tarda = round((cantidad / eg.eficiencia) + 0.5) + 2
            hoy = datetime.now()
            while dias_tarda > 0:
                hoy += timedelta(days=1)
                dia_semana = hoy.weekday()
                if dia_semana >= 5:
                    continue
                dias_tarda -= 1
            instance.fechaEstimada = hoy
            instance.save()

