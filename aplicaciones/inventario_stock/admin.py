from django.contrib import admin
from .models import *

# Register your models here.

#Aqui registramos los elementos para que aparezcan en el admin de django
admin.site.register(Calidad)
admin.site.register(Categoria)
admin.site.register(Modelo)
admin.site.register(Talla)
admin.site.register(Color)
admin.site.register(Proveedor)
admin.site.register(Ubicacion)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Inventario)