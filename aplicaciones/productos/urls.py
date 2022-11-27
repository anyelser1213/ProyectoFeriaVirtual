from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasProductos

app_name ="productos"

urlpatterns = [
    

    #Para los productos
    path('ProductoCrear/', vistasProductos.ProductosCrear.as_view() ,name="ProductosCrear"),
    path('ProductoListar/', vistasProductos.Productoslistar.as_view() ,name="ProductoListar"),

    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)