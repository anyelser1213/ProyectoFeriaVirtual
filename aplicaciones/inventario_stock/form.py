from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.peticiones.models import Peticion
from aplicaciones.inventario_stock.models import *
from aplicaciones.usuarios.models import *



###################### AQUI COMIENZAN LOS FORMULARIOS PARA TODO DE INVENTARIO ##########################################



class InventarioForm(ModelForm):


    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(InventarioForm, self).__init__(*args, **kwargs)
        print("Formulario InventarioForm: \n")
        print("usuario: ",self.usuario)
        #print("usuario ID: ",self.usuarioID.id)

        self.fields['productor_id'].empty_label = None
        self.fields['productor_id'].queryset = Usuarios.objects.filter(id=self.usuario.id)

        self.fields['producto_id'].empty_label = None

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Inventario
        fields = "__all__"
        widgets = {
            "productor_id": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),#display:none
            "producto_id": forms.Select(attrs={'class': 'form-select','style': ''  }),
            "cantidad": forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingresa Cantidad','min':1,'min_value':1}),
            "calidad": forms.Select(attrs={'class': 'form-select','style': ''  }),
            "precio": forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingresa Cantidad','min':1,'min_value':1}),
            #"nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de producto'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            }




