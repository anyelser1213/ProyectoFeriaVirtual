from django.urls import path
from aplicaciones.inventario_stock.api.api import Calidad_api_view

urlpatterns = [

    #Normal

    #Apis
    path('calidad/',Calidad_api_view,name='jugadaApi'),
    #path('consultarjugada/',consultarJugada_api_view,name='consultar_jugada'),
    #path('jugada/',JugadaApiView.as_view(),name='jugadaApi')
]