from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasInventarioStock

app_name ="inventario_stock"

urlpatterns = [
    

    
    path('ProductoCrear/', vistasInventarioStock.ProductosCrear.as_view() ,name="ProductosCrear"),
    path('ProductoListar/', vistasInventarioStock.Productoslistar.as_view() ,name="ProductoListar"),

    



    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)