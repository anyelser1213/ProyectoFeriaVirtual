#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import View
from io import BytesIO
from io import StringIO


#Para los pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,A6, landscape, letter
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


#Para las tablas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.rl_config import defaultPageSize 
from reportlab.lib.units import inch

PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()




#Llamamos para probar
from aplicaciones.peticiones.models import Peticion,Productos_de_Peticion
 
class ReportePersonasPDF(View):  
     
    def cabecera(self,pdf,usuario,id_peticion):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/Maipo_grande.jpg'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 190, 90,preserveAspectRatio=True)   

        #Pedimos Datos
        #Pedimos la informacion para almacenar
        Peticion_actual = Peticion.objects.get(id=id_peticion) 



        #pdf.drawString(60, 700, u"Cliente: "+str(usuario.username).title())
        #pdf.drawString(60, 670, u"Estatus: "+str(Peticion_actual.estado_peticion).title())
        
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"Reporte de la peticion #00"+str(id_peticion))
        pdf.drawString(230, 770, u"Cliente: "+str(usuario.username).title())
        pdf.drawString(230, 750, u"Status: "+str(Peticion_actual.estado_peticion).title())
        pdf.setFont("Helvetica", 14)
        #pdf.drawString(200, 770, u"REPORTE DE PERSONAS")            

    



    def tabla(self,pdf,id_peticion):




        cm = 20


        #Creamos una tabla para informacion del cliente
        #Establecemos el tamaño de cada una de las columnas de la tabla
        #tabla_informacion = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 3 * cm, 3 * cm]
        pdf.setFont("Helvetica", 14)

        
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('#', 'Producto', 'Calidad', 'Cantidad(Kg)')

        #Para saber la cantidad maxima
        cantidad_productos = Productos_de_Peticion.objects.filter(id_peticion = int(id_peticion)).count()
        print(cantidad_productos)
        detalles = ([ ])
        #detalles = ([("d","s","d") ])
        #Creamos con for normal
        aux = 1
        for producto in Productos_de_Peticion.objects.filter(id_peticion = int(id_peticion)):
        #for n in range(1,10):

            detalles.extend([(aux,str(producto.id_producto.nombre).title(),str(producto.calidad).title(),producto.cantidad) ])
            #detalles.extend([(n," .."," .."," ..")])
            aux+=1

            if aux == 2:
                pass
                #pdf.showPage()


        #Creamos una lista de tuplas que van a contener a las personas
        #detalles = [(producto.id_peticion.id, str(producto.id_producto.nombre).title(), str(producto.calidad).title(),producto.cantidad) for producto in Productos_de_Peticion.objects.filter(id_peticion = int(id_peticion))]
        
        

        #detalles.extend([("","","Total:") ])
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 3 * cm, 4 * cm])
        #print(detalle_orden)
        #Aplicamos estilos a las celdas de la tabla
        
        



        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.blue), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)

        if cantidad_productos <=10:
            #Definimos la coordenada donde se dibujará la tabla
            detalle_orden.drawOn(pdf, 100,600)
        elif cantidad_productos > 10 and cantidad_productos<=20:
            detalle_orden.drawOn(pdf, 100,300)

        #Hasta ahora mostrara 20 elementos maximos


    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer,pagesize=A4,pageCompression=None)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        id_peticion = self.kwargs.get('pk',None) #Asi es como obtenemos los datos get
        #print("REPORTE POST: ",self.request.POST)
        self.cabecera(pdf,self.request.user,id_peticion)
        self.tabla(pdf,id_peticion)
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



####################################################

Title = "Hello world" 
pageinfo = "platypus example" 
def myFirstPage(canvas, doc):
    canvas.saveState()    
    canvas.setFont('Times-Bold',16)    
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)    
    canvas.setFont('Times-Roman',9)    
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)    
    canvas.restoreState()

def myLaterPages(canvas, doc):    
    canvas.saveState()    
    canvas.setFont('Times-Roman',9)    
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))    
    canvas.restoreState()


def viewPDF(request):

    
 
    return response
