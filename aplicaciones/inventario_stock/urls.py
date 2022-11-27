from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasInventarioStock

app_name ="inventario_stock"

urlpatterns = [

    #Para el inventario
    path('Inventario_asignar/', vistasInventarioStock.Inventario_asignar.as_view() ,name="InventarioAsignar"),
    path('InventarioListar/', vistasInventarioStock.Inventariolistar.as_view() ,name="InventarioListar"),
    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)