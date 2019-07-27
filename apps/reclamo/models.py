from django.db import models

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

class Reclamo(models.Model):

    def cod_reclamo():
        reclamo = Reclamo
        ult_reclamo = reclamo.objects.all().count()

        if not ult_reclamo:
            return 'CTR-0000'

        nro_reclamo = int(ult_reclamo)
        nvo_codreclamo = 'CTR-' + str(nro_reclamo).zfill(4) 

        return nvo_codreclamo

    codReclamo = models.CharField(max_length=8, default=cod_reclamo, primary_key=True)
    #codDetContrato = models.CharField(max_length=8)
    codCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,blank=True, null=True)
    nombreUsuario = models.CharField(max_length=20)
    descripcion = models.models.CharField(max_length=500)
