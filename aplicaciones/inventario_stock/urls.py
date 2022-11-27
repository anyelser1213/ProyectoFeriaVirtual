from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasInventarioStock

app_name ="inventario_stock"

urlpatterns = [

    #Para el inventario
    path('Inventario_asignar/', vistasInventarioStock.Inventario_asignar.as_view() ,name="InventarioAsignar"),
    path('InventarioListar/', vistasInventarioStock.Inventariolistar.as_view() ,name="InventarioListar"),

    #Para las ofertas nacionales e internacionales
    path('Ofertas_nacionales/', vistasInventarioStock.Ofertas_Nacionales.as_view() ,name="OfertasNacionales"),
    path('Ofertas_internacionales/', vistasInventarioStock.Ofertas_Internacionales.as_view() ,name="OfertasInternacionales"),



    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)