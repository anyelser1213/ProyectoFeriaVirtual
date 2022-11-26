from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasInventarioStock

app_name ="inventario_stock"

urlpatterns = [
    

    #Para los productos
    path('ProductoCrear/', vistasInventarioStock.ProductosCrear.as_view() ,name="ProductosCrear"),
    path('ProductoListar/', vistasInventarioStock.Productoslistar.as_view() ,name="ProductoListar"),


    #Para las peticiones
    path('PeticionCrear/', vistasInventarioStock.PeticionCrear.as_view() ,name="PeticionCrear"),
    path('PeticionListar/', vistasInventarioStock.Peticionlistar.as_view() ,name="PeticionListar"),


    #Para el inventario
    path('Inventario_asignar/', vistasInventarioStock.Inventario_asignar.as_view() ,name="InventarioAsignar"),
    path('InventarioListar/', vistasInventarioStock.Inventariolistar.as_view() ,name="InventarioListar"),

    



    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)