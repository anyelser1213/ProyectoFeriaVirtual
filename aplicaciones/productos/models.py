from django.db import models

# Create your models here.


#el producto es para saber que tipo de mercancia tenemos
class Producto(models.Model):


    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        #return str(self.id_jugada)+" "+str(self.id_telefono)+" Usuario: "+str(self.id_usuario)
        return str(self.nombre).title()


