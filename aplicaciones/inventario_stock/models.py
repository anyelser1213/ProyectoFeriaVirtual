from django.db import models
from django.conf import settings
#from aplicaciones.usuarios.models import Usuarios

# Create your models here.
#el producto es para saber que tipo de mercancia tenemos
class Producto(models.Model):


    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        #return str(self.id_jugada)+" "+str(self.id_telefono)+" Usuario: "+str(self.id_usuario)
        return str(self.nombre).title()

class Peticion(models.Model):

    status_peticion = [
        ('revision','Revisión'),
        ('aprobada','Aprobada'),
        ('oferta','Oferta'),
        ('proceso','En proceso de atención'),
        ('atendida','Atendida'),
        ('cancelada','Cancelada'),
    ]

    #Para determinar que calidad tienen las frutas
    calidad_producto = [
        ('alta','Alta'),
        ('mediana','Mediana'),
        ('baja','Baja'),
    ]
    

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="cliente_peticion", on_delete=models.CASCADE,blank=True, null=True)
    productor_elegido = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="productor_peticion", on_delete=models.CASCADE,blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=False, null=False)
    calidad = models.CharField("calidad",max_length=150,choices=calidad_producto,default='baja',blank=True, null=True)
    cantidad = models.IntegerField(default=0,blank=False,null=False) #En base a Kilogramos(kg)

    aprobado_por = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="aprobado_por", on_delete=models.CASCADE,blank=True, null=True)
    estado_peticion = models.CharField("estado",max_length=150,choices=status_peticion,default='revision',blank=True, null=True)
    #fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    def __str__(self):
         return "Peticion de : "+str(self.cliente.username)+", Estatus: "+str(self.estado_peticion)

    class Meta:

        verbose_name = "Peticion"
        verbose_name_plural = "Peticiones"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            ("peticiones", "Peticiones"),
            #("consultarjugada", "ConsultarJugada"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos


#Estos contratos pueden ser para productores o clientes
class Contrato(models.Model):

    status = [
        ('vigente','Vigente'),
        ('caducado','Caducado'),
    ]

    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    estado_contrato = models.CharField("estatus",max_length=150,choices=status,default='caducado',blank=True, null=True)
    fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    def __str__(self):
         return "Usuario: "+str(self.usuario.username)+", Estatus: "+str(self.estado_contrato)

    class Meta:

        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarjugada", "ConsultarJugada"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos












#el inventario es para saber los patrimonios de la empresa
class Inventario(models.Model):

    #(Lo que se guarda en bases de datos, lo que se ve al usuario)
    status_producto = [
        ('vendido','Vendido'),
        ('danado','Dañado'),
        ('disponible','Disponible'),
    ]

    #Para determinar que calidad tienen las frutas
    calidad_producto = [
        ('alta','Alta'),
        ('mediana','Mediana'),
        ('baja','Baja'),
    ]

    id = models.AutoField(primary_key=True)
    productor_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    producto_id = models.ForeignKey("Producto", on_delete=models.CASCADE,blank=True, null=True)
    #ubicacion_id = models.ForeignKey("Ubicacion", on_delete=models.CASCADE)
    peso_cantidad = models.FloatField(default=0) #Para saber cantidad disponible de un producto (gramos)
    calidad = models.CharField("calidad",max_length=150,choices=calidad_producto,default='baja',blank=True, null=True)
    precio = models.FloatField(default=0,blank=True,null=True)


    #status = models.CharField("status",max_length=150,choices=status_producto,default='disponible',blank=True, null=True)

    def __str__(self):
        #return str(self.id_jugada)+" "+str(self.id_telefono)+" Usuario: "+str(self.id_usuario)
        return "id: "+str(self.id)+", Productor: "+str(self.productor_id.nombre)+",  "+str(self.producto_id)+", peso/cantidad:  "+str(self.peso_cantidad)+", Calidad: "+str(self.calidad)+", Precio:  "+str(self.precio)





















#################################################################################################

"""
class Contrato_cliente(models.Model):

    status = [
        ('vigente','Vigente'),
        ('caducado','Caducado'),
        ('finalizado','Finalizado'),
    ]

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="cliente", on_delete=models.CASCADE,blank=True, null=True)
    estado_contrato = models.CharField("estatus",max_length=150,choices=status,default='caducado',blank=True, null=True)
    fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    class Meta:

        verbose_name = "Contrato Cliente"
        verbose_name_plural = "Contratos Clientes"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarjugada", "ConsultarJugada"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos
"""






