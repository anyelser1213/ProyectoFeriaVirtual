from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasInventarioStock

app_name ="inventario_stock"

urlpatterns = [
    

    
    path('ProductorCrear/', vistasInventarioStock.ProductoresCrear.as_view() ,name="ProductoresCrear"),
    #path('CalidadListar/', vistasInventarioStock.CalidadListar.as_view() ,name="CalidadListar"),

    



    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)