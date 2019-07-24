from django.db import models

# Create your models here.
class RespuestaPredefinida(models.Model):

    def codRespuestaP():
        respuestap = RespuestaPredefinida
        ult_respuestap = respuestap.objects.all().count()

        if not ult_respuestap:
            return 'EMP-0000'

        nro_respuestap = int(ult_respuestap)
        nvo_codrespuestap = 'EMP-' + str(nro_respuestap).zfill(4) 

        return nvo_codrespuestap

    codRespuestaP = models.CharField(max_length=8, default=codRespuestaP, primary_key=True)
    descripcion = models.CharField(max_length=20)
    contUso = models.IntegerField()
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')