import json

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from aplicaciones.inventario_stock.models import Calidad
from aplicaciones.inventario_stock.api.serializers import JugadaSerializer

@api_view(['GET','POST'])
def inventario_api_view(request):


    if request.method == 'GET':
        jugadas = Calidad.objects.all()
        jugadas_serializer = JugadaSerializer(jugadas,many=True)
        return Response(jugadas_serializer.data)
    
    elif request.method == 'POST':


        datos={}
        #jugada_serializer = JugadaSerializer(data = request.data) #De json a objeto otra ves y guardamos
        

        #print("El tipo de dato es: ",type(datos))

        return JsosResponse(datos,safe = False)
        #return HttpResponse(json.dumps(data), content_type = "application/json")
        """
        data={'uno':1,'dos':2}
        return JsonResponse(data,safe = False)
        
        
        if jugada_serializer.is_valid(): #Verificamos que la data es correcta
            #jugada_serializer.save() #Guardamos la data en base de datos
            return Response(jugada_serializer.data)
        else:
            return Response(jugada_serializer.errors)
        print(request.data)
        """


"""
class JugadaApiView(APIView):

    def get(self, request):
        jugadas = Jugada.objects.all()
        jugadas_serializer = JugadaSerializer(jugadas,many=True)
        return Response(jugadas_serializer.data)
"""








@api_view(['GET','POST'])
def consultarCalidad_api_view(request):


    #if request.method == 'GET':
    #    jugadas = Jugada.objects.all()
    #    jugadas_serializer = JugadaSerializer(jugadas,many=True)
    #    return Response(jugadas_serializer.data)
    
    if request.method == 'POST':

        #print("datos",request.data, "Usuario: ",request.user.username, " Id:",request.user.id)
        #print("datos tipos:  ",request.data.get('tipos'))
        tipos = request.data.get('tipos')

        #Datos que enviaremos
        datos = {}

        jugadas_serializer = JugadaSerializer(datos,many=True) #El many true es cuando son varios objetos
        
        #print(jugadas_serializer)
        #print(jugadas_serializer.data)

        return JsonResponse(jugadas_serializer.data,safe = False)
