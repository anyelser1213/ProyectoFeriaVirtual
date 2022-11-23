from django.db import models
from django.conf import settings
#from aplicaciones.usuarios.models import Usuarios

# Create your models here.
'''
#La calidad se refiere al tipo de material
class Calidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

#la categoria indica si es damas, caballeros, o ninos
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

#el modelo se refiere al tipo del producto, ejemplo: Camiseta cuello v
class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

#la talla indica si es s,m,l, etc
class Peso(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.CharField(max_length=100,unique=True)

#el color es para colocar color exacto al producto
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)
    codigo_hex = models.CharField(max_length=100,unique=True)


#El cliente es para saber quien nos compra
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cedula = models.PositiveIntegerField(unique=True)
    direccion = models.CharField(max_length=100,blank=True, null=True)
    telefono = models.CharField(max_length=100,blank=True, null=True)


#el proveedor es para saber quien nos da el producto
class Productor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)
    rif = models.CharField(max_length=100,unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)





    
    nombre = models.CharField(max_length=100)
    cedula = models.PositiveIntegerField(unique=True)
    direccion = models.CharField(max_length=100,blank=True, null=True)
    telefono = models.CharField(max_length=100,blank=True, null=True)
   

#el producto es para saber que tipo de mercancia tenemos
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)
    calidad_id = models.ForeignKey("Calidad", on_delete=models.CASCADE,blank=True, null=True)
    categoria_id = models.ForeignKey("Categoria", on_delete=models.CASCADE,blank=True, null=True)
    modelo_id = models.ForeignKey("Modelo", on_delete=models.CASCADE,blank=True, null=True)
    peso_id = models.ForeignKey("Peso", on_delete=models.CASCADE,blank=True, null=True)
    color_id = models.ForeignKey("Color", on_delete=models.CASCADE,blank=True, null=True)
    #ubicacion_id = models.ForeignKey("Ubicacion", on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey("Productor", on_delete=models.CASCADE) 


#el stock es para saber cuantos productos tenemos disponibles
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)
    producto_id = models.ForeignKey("Producto", on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField (default=0,null=False)

#el inventario es para saber los patrimonios de la empresa
class Inventario(models.Model):

    #(Lo que se guarda en bases de datos, lo que se ve al usuario)
    status_producto = [
        ('vendido','Vendido'),
        ('danado','Dañado'),
        ('disponible','Disponible'),
    ]

    id = models.AutoField(primary_key=True)
    producto_id = models.ForeignKey("Producto", on_delete=models.CASCADE)
    ubicacion_id = models.ForeignKey("Ubicacion", on_delete=models.CASCADE)
    status = models.CharField("status",max_length=150,choices=status_producto,default='disponible',blank=True, null=True)
    
#la ubicacion es para saber en que parte de un lugar se encuentra algo
class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    piso = models.CharField(max_length=100)

    
 '''






class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="cliente", on_delete=models.CASCADE,blank=True, null=True)
    productor = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="productor", on_delete=models.CASCADE,blank=True, null=True)