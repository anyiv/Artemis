from django.db import models

class Oficina(models.Model):

    def cod_Oficina():
        oficina = Oficina
        ult_oficina = oficina.objects.all().count()

        if not ult_oficina:
            return 'OFI-0000'

        nro_oficina = int(ult_oficina)
        nvo_codoficina = 'OFI-' + str(nro_oficina).zfill(4) 

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

class Estado(models.Model):

    def cod_Estado():
        ult_estado = Estado.objects.all().count()

        if not ult_estado:
            return 'EST-0000'

        nro_estado = int(ult_estado)
        nvo_codestado = 'EST-' + str(nro_estado).zfill(4) 

        return nvo_codestado

    codEstado = models.CharField(max_length=8,primary_key=True,default=cod_Estado)
    nombre = models.CharField(max_length=40)
    ESTATUS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS,default='A')

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):

    def cod_Ciudad():
        ult_ciudad = Ciudad.objects.all().count()

        if not ult_ciudad:
            return 'CIU-0000'

        nro_ciudad = int(ult_ciudad)
        nvo_codciudad = 'CIU-' + str(nro_ciudad).zfill(4) 

        return nvo_codciudad

    codCiudad = models.CharField(max_length=8,primary_key=True,default=cod_Ciudad)
    codEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    ESTATUS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS,default='A')

    def __str__(self):
        return self.nombre

class Zona(models.Model):

    def cod_Zona():
        ult_zona = Zona.objects.all().count()

        if not ult_zona:
            return 'ZON-0000'

        nro_zona = int(ult_zona)
        nvo_codzona = 'ZON-' + str(nro_zona).zfill(4) 

        return nvo_codzona

    codZona = models.CharField(max_length=8,primary_key=True,default=cod_Zona)
    codCiudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    ESTATUS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS,default='A')

    def __str__(self):
        return self.nombre

class Contrato(models.Model):
    nroContrato = models.AutoField(primary_key=True)
    codCliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    codZona = models.ForeignKey(Zona,on_delete=models.CASCADE)
    nroAsociado = models.CharField(max_length=10)
    ESTATUS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS,default='A')

    def __str__(self):
        return str(self.nroContrato)

class Servicio(models.Model):

    def cod_Servicio():
        ult_servicio = Servicio.objects.all().count()

        if not ult_servicio:
            return 'SER-0000'

        nro_servicio = int(ult_servicio)
        nvo_codservicio = 'SER-' + str(nro_servicio).zfill(4) 

        return nvo_codservicio

    codServicio = models.CharField(max_length=8,primary_key=True,default=cod_Servicio)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=120)
    ESTATUS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS,default='A')

    def __str__(self):
        return self.nombre

class DetalleContrato(models.Model):
    def cod_DetCont():
        ult_dc = DetalleContrato.objects.all().count()

        if not ult_dc:
            return 'DC-0000'

        nro_dc = int(ult_dc)
        nvo_dc = 'DC-' + str(nro_dc).zfill(4) 

        return nvo_dc

    codDetContrato = models.CharField(max_length=8,primary_key=True,default=cod_DetCont)
    nroContrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)
    codServicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)

    def __str__(self):
        return self.codDetContrato + '/' + str(self.nroContrato)
