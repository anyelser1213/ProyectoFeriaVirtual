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

    #Para determinar que calidad tienen las frutas
    tipo_peticion = [
        ('nacional','Nacional'),
        ('internacional','Internacional'),
    ]
    

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="cliente_peticion", on_delete=models.CASCADE,blank=True, null=True)
    productor_elegido = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="productor_peticion", on_delete=models.CASCADE,blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=False, null=False)
    calidad = models.CharField("calidad",max_length=150,choices=calidad_producto,default='baja',blank=False, null=False)
    cantidad = models.IntegerField(default=1,blank=False,null=False) #En base a Kilogramos(kg)

    aprobado_por = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="aprobado_por", on_delete=models.CASCADE,blank=True, null=True)
    estado_peticion = models.CharField("estado",max_length=150,choices=status_peticion,default='revision',blank=True, null=True)
    tipo_peticion = models.CharField("tipo",max_length=150,choices=tipo_peticion,default='nacional',blank=True, null=True)
    #fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    def __str__(self):
         return "Peticion de : "+str(self.cliente.username)+" Producto: "+str(self.producto.nombre)+", Cantidad: "+str(self.cantidad)+"Kg"+", Estatus: "+str(self.estado_peticion)+", Tipo: "+str(self.tipo_peticion)

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




class Ofertas_Productores(models.Model):


    #Con esto determinamos en que proceso se encuentra la peticion
    status_oferta = [
        ('revision','Revisión'), #El administrador debe validar la petición
        ('aprobada','Aprobada'),
        ('anulado','Anulado'),
        
    ]

    #Para determinar que calidad tienen las frutas
    calidad_producto = [
        ('alta','Alta'),
        ('mediana','Mediana'),
        ('baja','Baja'),
    ]

    

    id = models.AutoField(primary_key=True)
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE,blank=True, null=True)
    productor = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="productor_oferta", on_delete=models.CASCADE,blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=False, null=False)
    calidad = models.CharField("calidad",max_length=150,choices=calidad_producto,default='baja',blank=False, null=False)
    cantidad = models.IntegerField(default=1,blank=False,null=False) #En base a Kilogramos(kg)
    precio_kilo = models.FloatField(default=1,blank=True,null=True) #Precio por Kilo

    oferta_aprobado_por = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="oferta_aprobado_por", on_delete=models.CASCADE,blank=True, null=True)
    estado_oferta = models.CharField("estado",max_length=150,choices=status_oferta,default='revision',blank=True, null=True)
    #fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    def __str__(self):


        #x = range(1,self.cantidad+1)
        #aux =0
        #for n in x:
        #    aux =1

        return "Oferta de : "+str(self.productor.username)+" ----- Producto: "+str(self.producto.nombre)+" ----- Calidad: "+str(self.calidad)+" ----- Cantidad: "+str(self.cantidad)+"Kg"+" ----- Estatus: "+str(self.estado_oferta)+"----- Precio Kilo: "+str(self.precio_kilo) +"CLP, ----- Total: "+str(float(self.precio_kilo*self.cantidad))+"CLP"

    class Meta:

        verbose_name = "Oferta Productor"
        verbose_name_plural = "Ofertas Productores"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("peticiones", "Peticiones"),
            #("consultarjugada", "ConsultarJugada"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos



class Ofertas_Transportistas(models.Model):


    #Con esto determinamos en que proceso se encuentra la peticion
    status_oferta = [
        ('revision','Revisión'), #El administrador debe validar la petición
        ('aprobada','Aprobada'),
        ('anulado','Anulado'),
        
    ]

    #Para determinar que calidad tienen las frutas
    calidad_envio = [
        ('alta','Alta'),
        ('mediana','Mediana'),
        ('baja','Baja'),
    ]

    

    id = models.AutoField(primary_key=True)
    peticion = models.ForeignKey(Peticion, on_delete=models.CASCADE,blank=True, null=True)
    transportista = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="transportista_oferta", on_delete=models.CASCADE,blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=False, null=False)
    calidad_envio = models.CharField("calidad",max_length=150,choices=calidad_envio,default='baja',blank=False, null=False)
    cantidad = models.IntegerField(default=1,blank=False,null=False) #En base a Kilogramos(kg)
    precio_envio = models.FloatField(default=1,blank=True,null=True) #Precio por Kilo
    direccion_origen = models.TextField(default="Origen Desconocido")
    direccion_destino = models.TextField(default="Destino Desconocido",blank=False,null=False)
    oferta_transporte_aprobado_por = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="oferta_transporte_aprobado_por", on_delete=models.CASCADE,blank=True, null=True)
    estado_oferta = models.CharField("estado",max_length=150,choices=status_oferta,default='revision',blank=True, null=True)
    #fecha_caducidad = models.DateField(auto_now_add=False,auto_now=False,blank=True) #Solo fecha

    def __str__(self):


        #x = range(1,self.cantidad+1)
        #aux =0
        #for n in x:
        #    aux =1

        return "Oferta de : "+str(self.transportista.username)+" ----- Producto: "+str(self.producto.nombre)+" ----- Calidad: "+str(self.calidad)+" ----- Cantidad: "+str(self.cantidad)+"Kg"+" ----- Estatus: "+str(self.estado_oferta)+"----- Precio Kilo: "+str(self.precio_kilo) +"CLP, ----- Total: "+str(float(self.precio_kilo*self.cantidad))+"CLP"

    class Meta:

        verbose_name = "Oferta Transportista"
        verbose_name_plural = "Ofertas Transportistas"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("peticiones", "Peticiones"),
            #("consultarjugada", "ConsultarJugada"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos

