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

class Empleado(models.Model):

    def cod_Empleado():
        empleado = Empleado
        ult_empleado = empleado.objects.all().count()

        if not ult_empleado:
            return 'EMP-0000'

        nro_empleado = int(ult_empleado)
        nvo_codempleado = 'EMP-' + str(nro_empleado).zfill(4) 

        return nvo_codempleado

    codEmpleado = models.CharField(max_length=8, default=cod_Empleado, primary_key=True)
    codOficina = models.ForeignKey(Oficina,on_delete=models.CASCADE)    
    identificacion = models.CharField(max_length=15)    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60,default='Barquisimeto')
    correo = models.EmailField(max_length=30,default='correo@artemis.com')
    telefono = models.CharField(max_length=11)
    CARGOS = ( 
        ('ger','Gerente'),
        ('admin','Administrador del Sistema'),
        ('gestorr','Gestor de reclamos'),
        ('gestorpqs','Gestor de PQS'),
        ('atencioncli','Atención al cliente'),
        ('tec','Técnico'),
    )
    cargo = models.CharField(max_length=20, choices=CARGOS, blank=False, null=False)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

class Cliente(models.Model):

    def cod_Cliente():
        cliente = Cliente
        ult_cliente = cliente.objects.all().count()

        if not ult_cliente:
            return 'CLI-0000'

        nro_cliente = int(ult_cliente)
        nvo_codcliente = 'EMP-' + str(nro_cliente).zfill(4) 

        return nvo_codcliente

    codCliente = models.CharField(max_length=8, default=cod_Cliente, primary_key=True)
    identificacion = models.CharField(max_length=15)    
    nombre = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60,default='Barquisimeto')
    correo = models.EmailField(max_length=30,default='correo@artemis.com')
    telefono = models.CharField(max_length=11)
    ESTATUS = ( 
        ('A','Activo'),
        ('I','Inactivo'),
    )
    estatus = models.CharField(max_length=1,choices=ESTATUS, default='A')

