from django.contrib import admin
from .models import *

# Register your models here.

#Aqui registramos los elementos para que aparezcan en el admin de django
#admin.site.register(Contrato_productor)
admin.site.register(Contrato)
admin.site.register(Producto)
admin.site.register(Inventario)