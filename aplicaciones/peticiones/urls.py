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
    #Url para ver procesos de una peticion
    path('Peticion_Procesos/<int:pk>/', vistasPeticiones.Peticion_Procesos_View.as_view() ,name="Peticion_Procesos"),

    #Url para ver aprobar una peticion
    path('Peticion_Aprobar/<int:pk>/', vistasPeticiones.Peticion_Aprobar ,name="Peticion_Aprobar"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)