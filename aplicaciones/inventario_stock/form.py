from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.inventario_stock.models import *
from aplicaciones.usuarios.models import *



###################### AQUI COMIENZAN LOS FORMULARIOS PARA TODO DE INVENTARIO ##########################################

class ProductoForm(ModelForm):


    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(ProductoForm, self).__init__(*args, **kwargs)
        print("Formulario ProductoForm: \n")
        #print("usuario: ",self.usuarioID)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Producto
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de producto'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }

class PeticionForm(ModelForm):


    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario',None)
        #self.usuarioID = kwargs.pop('user',None)
        super(PeticionForm, self).__init__(*args, **kwargs)
        print("Formulario PeticionForm: ")
        print("usuario : ",self.usuario)
        #print("usuario ID: ",self.usuarioID.id)

        self.fields['cliente'].empty_label = None
        self.fields['cliente'].queryset = Usuarios.objects.filter(id=self.usuario.id)

        self.fields['producto'].empty_label = None

        self.fields['calidad'].empty_label = None
        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Peticion
        fields = "__all__"
        widgets = {
            "cliente": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),#display:none
            "productor_elegido": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),#display:none
            "producto": forms.Select(attrs={'class': 'form-select','style': ''  }),#display:none
            "calidad": forms.Select(attrs={'class': 'form-select','style': 'color:red'   }),
            "cantidad": forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingresa Cantidad','min':1,'min_value':1}),
            "aprobado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),#display:none
            "estado_peticion": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            
            #"estado_peticion": forms.Select(attrs={'class': 'form-select','style': ''  }),
        }

class InventarioForm(ModelForm):


    def __init__(self, *args, **kwargs):
        #usuario_id = kwargs.pop('usuario')
        #self.usuarioID = kwargs.pop('user')
        super(InventarioForm, self).__init__(*args, **kwargs)
        print("Formulario InventarioForm: \n")
        #print("usuario: ",self.usuarioID)
        #print("usuario ID: ",self.usuarioID.id)

        #self.fields['creado_por'].empty_label = None
        #self.fields['creado_por'].queryset = Usuarios.objects.filter(id=self.usuarioID.id)

        #self.fields['imagen'].widget.attrs.update({'class': 'form-control ' })

    class Meta:

        model = Inventario
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa nombre de producto'}),
            #"direccion": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter company address'}),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            #"creado_por": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
        }

