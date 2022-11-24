from django.contrib import admin
from .models import *

# Register your models here.

#Aqui registramos los elementos para que aparezcan en el admin de django
admin.site.register(Contrato_vigencia)
admin.site.register(Contrato_cliente)
#admin.site.register(Modelo)
#admin.site.register(Peso)
#admin.site.register(Color)

#admin.site.register(Productor)
#admin.site.register(Ubicacion)
#admin.site.register(Cliente)
admin.site.register(Producto)


#admin.site.register(Stock)
admin.site.register(Inventario)