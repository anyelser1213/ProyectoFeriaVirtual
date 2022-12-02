from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasPeticiones

app_name ="ofertas"

urlpatterns = [


     #Para las ofertas nacionales e internacionales
    path('Ofertas_nacionales/', vistasPeticiones.Ofertas_Nacionales.as_view() ,name="OfertasNacionales"),
    path('Ofertas_internacionales/', vistasPeticiones.Ofertas_Internacionales.as_view() ,name="OfertasInternacionales"),

    #Ofertas que lanzan los productores
    #path('Productor_oferta/', vistasPeticiones.Ofertas_Internacionales.as_view() ,name="OfertasInternacionales"),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)