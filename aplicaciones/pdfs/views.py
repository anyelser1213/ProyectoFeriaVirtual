#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import View
from io import BytesIO


#Para los pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,A6, landscape, letter
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


#Para las tablas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph




#Llamamos para probar
from aplicaciones.peticiones.models import Peticion
 
class ReportePersonasPDF(View):  
     
    def cabecera(self,pdf,id):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/Maipo_grande.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)    

        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"Reporte de la peticion #00"+str(id))
        pdf.setFont("Helvetica", 14)
        #pdf.drawString(200, 770, u"REPORTE DE PERSONAS")            

    



    def tabla(self,pdf,y):

        cm = 20
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('DNI', 'Nombre', 'Apellido Paterno', 'Apellido Materno')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(persona.id, persona.cliente.username, persona.revision) for persona in Peticion.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.blue), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 100,y)


    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        #print("REPORTE id: ",self.kwargs.get('pk',None))
        id_peticion = self.kwargs.get('pk',None) #Asi es como obtenemos los 
        #print("REPORTE POST: ",self.request.POST)
        self.cabecera(pdf,id_peticion)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response






""" OTRA FORMA CON LOS PDF"""



class CustomDocTemplate(SimpleDocTemplate):
    def __init__(
        self,
        filename,
        right_margin=7,
        left_margin=7,
        top_margin=7,
        bottom_margin=7,
        pagesize=landscape(A4),
        **kw,
    ):
        super().__init__(filename, **kw)
        self.rightMargin = right_margin
        self.leftMargin = left_margin
        self.topMargin = top_margin
        self.bottomMargin = bottom_margin
        self.pagesize = A4 #Tipo de hoja


class A4Printer:
    def get_pdf(self, buffer):
        self.buffer = buffer
        styles = getSampleStyleSheet()
        doc = CustomDocTemplate(buffer)
        elements = []
        elements.append(Paragraph("Title of the PDF", style=styles["Heading2"]))
        elements.append(Paragraph("Heading", style=styles["Heading4"]))
        elements.append(Paragraph("Text inside the pdf", style=styles["BodyText"]))
        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf


class A4View(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="Example.pdf"'
        print(self.request.GET)
        print("Buscando la variable> ",self.kwargs.get('pk',None))
        a4p = A4Printer()
        pdf = a4p.get_pdf(BytesIO())
        response.write(pdf)
        return response


##########################################


