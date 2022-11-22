from dataclasses import fields
from rest_framework import serializers
from aplicaciones.inventario_stock.models import Jugada


class JugadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugada
        #fields = '__all__'
        fields = ['digitos','repetidor'] #cuando son campos especificos
        
        #exclude