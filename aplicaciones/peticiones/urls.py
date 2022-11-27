from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasPeticiones

app_name ="peticiones"

urlpatterns = [
    

    #Para las peticiones
    path('PeticionCrear/', vistasPeticiones.PeticionCrear.as_view() ,name="PeticionCrear"),
    path('PeticionListar/', vistasPeticiones.Peticionlistar.as_view() ,name="PeticionListar"),



    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)