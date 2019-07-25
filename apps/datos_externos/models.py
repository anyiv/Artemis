from django.db import models

class Oficina(models.Model):

    def cod_Oficina():
        oficina = Oficina
        ult_oficina = oficina.objects.all().count()

        if not ult_oficina:
            return 'OFI-0000'

        nro_oficina = int(ult_oficina)
        nvo_codoficina = 'EMP-' + str(nro_oficina).zfill(4) 

        return nvo_codoficina

    codOficina = models.CharField(max_length=8, default=cod_Oficina, primary_key=True)
    #codZona = models.ForeignKey()
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30,default='Barquisimeto')
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=11)
    codOficina = models.ForeignKey(Oficina,on_delete=models.CASCADE)    
    cargo = models.CharField(max_length=60, blank=False, null=False)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

    def __str__(self):
        return self.nombre +' '+ self.apellido

class Cliente(models.Model):
    identificacion = models.CharField(max_length=15, primary_key=True)    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=11)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

    def __str__(self):
        return self.nombre +' '+ self.apellido