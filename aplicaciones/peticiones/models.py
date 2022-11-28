from django.db import models
from django.conf import settings

from aplicaciones.productos.models import Producto

# Create your models here.


class Peticion(models.Model):


    #Con esto determinamos en que proceso se encuentra la peticion
    status_peticion = [
        ('revision','Revisión'), #El administrador debe validar la petición
        #('aprobada','Aprobada'),
        ('oferta','Oferta'), #Los productores pueden ver y ofertar
        ('transporte','Transporte'),#La peticion se hace visible para los transportistas y pueden ofertar para enviar la mercancia
        ('proceso','Proceso de verificación'), #Proceso de verificación
        ('atendida','Atendida'),
        ('cancelada','Cancelada'),
    ]

    #Para determinar que calidad tienen las frutas
    tipo_peticion = [
        ('nacional','Nacional'),
        ('internacional','Internacional'),
    ]
    

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="cliente_peticion", on_delete=models.CASCADE,blank=True, null=True)
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=False, null=False)
    
    
    tabla_Productos = models.ManyToManyField(Producto,through='Productos_de_Peticion')
    

    #Cada campos re presenta es un proceso de la peticion 
    
    #Proceso de revision con su admin aprobador
    revision = models.BooleanField(default=False)
    aprobado_por = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="aprobado_por", on_delete=models.CASCADE,blank=True, null=True)
    
    #Proceso de oferta con su productor
    oferta = models.BooleanField(default=False)
    productor_elegido = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="productor_peticion", on_delete=models.CASCADE,blank=True, null=True)
    
    #Proceso de transporte con su transportista
    transporte = models.BooleanField(default=False)
    transportista_elegido = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="transportista_peticion", on_delete=models.CASCADE,blank=True, null=True)
    
    #Proceso de verificacion(se lleva a cabo la verificacion)
    proceso_de_verificacion = models.BooleanField(default=False)

    #Proceso de finalización(El cliente aprueba el envio de la mercancia)
    atendido = models.BooleanField(default=False)
    


    
    
    
    #Este campo es para saber en que proceso estamos
    estado_peticion = models.CharField("estado",max_length=150,choices=status_peticion,default='revision',blank=True, null=True)
    tipo_peticion = models.CharField("tipo",max_length=150,choices=tipo_peticion,default='nacional',blank=True, null=True)
    #fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    def __str__(self):
         return "Peticion de : "+str(self.cliente.username)+", Estatus: "+str(self.estado_peticion)+", Tipo: "+str(self.tipo_peticion)

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




class Productos_de_Peticion(models.Model):

    #Para determinar que calidad tienen las frutas
    calidad_producto = [
        ('alta','Alta'),
        ('mediana','Mediana'),
        ('baja','Baja'),
    ]

    id_peticion = models.ForeignKey(Peticion,on_delete=models.CASCADE,blank=True, null=True)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True, null=True)

    calidad = models.CharField("calidad",max_length=150,choices=calidad_producto,default='baja',blank=False, null=False)
    cantidad = models.IntegerField(default=1,blank=False,null=False) #En base a Kilogramos(kg)
    #id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE,blank=True, null=True)
    #id_comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE,blank=True, null=True)

    #status = models.CharField("status",
    #    max_length=150,
    #    choices=tipo_plan,    
    #    default='Por Pagar'
    #)

    def __str__(self):
        return "Peticion de: "+str(self.id_peticion.cliente.username)+" ----- Pedido: "+str(self.id_producto)+" ----- Calidad:"+str(self.calidad)+" ----- Cantidad: "+str(self.cantidad)+"Kg"
        #return "id: "+str(self.id)+", Tipo Jugada: "+str(self.id_jugada.id_tipo_jugada)+", "+str(self.id_jugada)+" "+str(self.id_usuario)+" "+str(self.id_comprobante)+" "+str(self.id_telefono)+" Usuario: "+str(self.id_usuario)+" Status: "+self.status