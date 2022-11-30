from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasPdf

app_name ="pdfs"

urlpatterns = [


    #Para crear los pdfs con clases
    #path('pdf/', vistasPdf.ReportePersonasPDF.as_view() ,name="pdf"),

    #Con argumentos 
    path('pdf/<int:pk>', vistasPdf.ReportePersonasPDF.as_view() ,name="pdf"),

    path('pdf2/', vistasPdf.viewPDF  ,name="pdf2"),

    #path('pdf_3/', vistasPdf.PrivacyPaperPrinter.get_pdf ,name="pdf_3"),
    

    #Pruebas
     #path('pdf_prueba/', vistasPdf.crear_pdf ,name="pdf2"),


    #path('Ofertas_internacionales/', vistasPeticiones.Ofertas_Internacionales.as_view() ,name="OfertasInternacionales"),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)