from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ClearableFileInput, ModelForm, widgets
from aplicaciones.peticiones.models import *
from aplicaciones.usuarios.models import *



###################### AQUI COMIENZAN LOS FORMULARIOS PARA PETICIONES ##########################################


####################### FINALIZAMOS FORMULARIOS INDIVIDUALES #############################################

class PeticionPersonalizadoForm(forms.Form):

    #Para determinar que calidad tienen las frutas
    calidad_producto = [
        ('alta','Alta'),
        ('mediana','Mediana'),
        ('baja','Baja'),
    ]


    #nombre = forms.CharField(label='Nombre',max_length=30,error_messages={'required': 'no funciona asi'},widget=forms.TextInput(attrs={'placeholder':'Ingresa nombre de master'}))
    productos = forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    calidad = forms.ChoiceField(choices=calidad_producto,widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    cantidad = forms.FloatField(required=True, min_value=1, widget=forms.NumberInput(attrs={'class':'form-control','value':'1','id': 'form_homework', 'step': "0.01"})) 
    #rif_ci = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Ingresa tu cedula de identidad'}))
    #entidad_estatus = forms.ChoiceField(choices=entidad_estados)
    #email = forms.EmailField(initial='',widget=forms.EmailInput(attrs={'placeholder':'Ejemplo@gmail.com'}))
    #telefono = forms.IntegerField()
    #estado = forms.ModelChoiceField(Estado.objects.all(),empty_label=None,required=False)
    #ciudad = forms.ModelChoiceField(Ciudad.objects.all(),empty_label=None,required=False)
    #BotonFantasma = forms.BooleanField(required=False)
    #BotonFantasmaComer = forms.BooleanField(required=False)
    #descripcion = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ingresa tu Direccion '}))
    
    def __init__(self,*args,**kwargs):
        usuario = kwargs.pop('usuario')
        super(PeticionPersonalizadoForm,self).__init__(*args, **kwargs)
        
        self.fields['productos'].empty_label = None
        #self.fields['telefono'].widget.attrs['placeholder'] = "Ingresa tu numero telefonico"
        #self.fields['entidad_estatus'].initial= "Activo sin venta"
        #productos = forms.ModelChoiceField(queryset=Producto.objects.all())
        print(usuario)




class PeticionForm(ModelForm):


    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario',None)
        #self.usuarioID = kwargs.pop('user',None)
        super(PeticionForm, self).__init__(*args, **kwargs)
        print("Formulario PeticionForm: ")
        print("usuario : ",self.usuario)
        print("usuario nacionalidad : ",self.usuario.nacionalidad)
        #print("usuario ID: ",self.usuarioID.id)

        """
        for field in self.fields:
            # Recorremos todos los campos del modelo para a??adirle class="form-control
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        """

        self.fields['cliente'].empty_label = None
        self.fields['cliente'].queryset = Usuarios.objects.filter(id=self.usuario.id)

        #self.fields['producto'].empty_label = None

        #self.fields['calidad'].empty_label = None
        
        if self.usuario.nacionalidad == "chileno":
            CHOICES = (('nacional', 'Nacional'),)
            self.fields['tipo_peticion'].choices = CHOICES
        else:
            CHOICES = (('internacional','Internacional'),)
            self.fields['tipo_peticion'].choices = CHOICES
        
        
        
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
            "tipo_peticion": forms.Select(attrs={'class': 'form-select','style': 'display:none'  }),
            #"descripcion": forms.Textarea(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter company information'}),
            #"sitio_web": forms.TextInput(attrs={'class': 'form-control border-input','rows':'3','placeholder':'Enter website'}),
            #"color": forms.TextInput(attrs={'type': 'color', 'class':'form-control oculto2'}),
            #"imagenEmpresa": forms.ImageField(attrs={'class': 'form-control','placeholder':'Enter department image'}),
            #"imagenEmpresa":forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company image'}),
            #"videoEmpresa": forms.ClearableFileInput(attrs={'class': 'form-control oculto','placeholder':'Enter company video','accept':'video/*'}),
            
            #"estado_peticion": forms.Select(attrs={'class': 'form-select','style': ''  }),
        }
