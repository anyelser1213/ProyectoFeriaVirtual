from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasPeticiones

app_name ="peticiones"

urlpatterns = [
    

    #Para las peticiones
    path('PeticionCrear/', vistasPeticiones.PeticionCrear_def, name='PeticionCrear'),
    #path('PeticionCrear/', vistasPeticiones.PeticionCrear.as_view() ,name="PeticionCrear"),
    path('PeticionListar/', vistasPeticiones.Peticionlistar.as_view() ,name="PeticionListar"),

    #Url para ver productos de una peticion
    path('Peticion_Productos/<int:pk>/', vistasPeticiones.Peticion_Productos_View.as_view() ,name="Peticion_Productos"),


    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)