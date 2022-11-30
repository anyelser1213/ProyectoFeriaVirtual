from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasPdf

app_name ="pdfs"

urlpatterns = [


    #Para crear los pdfs
    path('pdf/', vistasPdf.some_view ,name="pdf"),
    #path('Ofertas_internacionales/', vistasPeticiones.Ofertas_Internacionales.as_view() ,name="OfertasInternacionales"),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)