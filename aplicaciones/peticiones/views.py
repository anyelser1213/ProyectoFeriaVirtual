from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy

#Aplicacion de PRODUCTOS
from aplicaciones.usuarios.models import Usuarios

#Aplicacion de PRODUCTOS
from aplicaciones.productos.models import Producto
from aplicaciones.productos.form import ProductoForm

#Aplicacion de PETICIONES
from aplicaciones.peticiones.models import Peticion, Productos_de_Peticion
from aplicaciones.peticiones.form import PeticionPersonalizadoForm,PeticionForm

#Aplicacion de ofertas
from aplicaciones.ofertas.models import Contrato



#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

# Create your views here.



######################## PARA LAS PETICIONES ################################################


def PeticionCrear_def(request):
    #verificamos que estamos ogeados
    if request.user.is_authenticated:
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("ENTRAMOS EN GET PARA CREAR LA PETICION")
            form = PeticionPersonalizadoForm(usuario=request.user)
            contexto = {'form': form,
                        'user': request.user}
            contexto['contrato'] ="SIN CONTRATO"

            contrato_usuario = Contrato.objects.filter(usuario=request.user)
            if contrato_usuario.exists():
                print("Si tiene contrato")
                
                #Verificamos si tiene el contrato vigente
                contrato_vigente = Contrato.objects.get(usuario=self.request.user)
                if contrato_vigente.estado_contrato == "vigente":
                    print("El contrato del usuario:",self.request.user.username,"SI esta vigente.")
                    contexto['ofertas'] = Peticion.objects.filter(tipo_peticion="nacional")
                    contexto['contrato'] ="CONTRATO VIGENTE"

                else:
                    print("El contrato del usuario:",self.request.user.username,"NO esta vigente.")
                    contexto['ofertas'] = Peticion.objects.none()
                    contexto['contrato'] ="CONTRATO CADUCADO"
            else:
                print("No tiene contrato")
                contexto['contrato'] ="SIN CONTRATO"
                #print("entramos en GET:", orden)






        #Metodo(POST)
        else:

            #print(request.POST)
            print("\nEntramos en POST de la peticion\n")
            print(request.POST)
            form = PeticionPersonalizadoForm(data=request.POST,usuario=request.user)

            #Variables para guardar
            productos = request.POST.getlist('productos')
            calidad = request.POST.getlist('calidad')
            cantidad = request.POST.getlist('cantidad')
            
            print(productos," jajajajaja")

            #si el formulario tiene los datos correctos entramos aqui
            
            
            
            if form.is_valid():
            # and trabajo.is_valid() and suministro.is_valid():
            
            
                print("\nEl formulario es correcto")

                #Creamos la peticion primero
                Peticion_Creada = Peticion.objects.create(cliente=request.user)


                #Con este for guardamos los productos en la peticion correspondiente
                for i in range(len(productos)):
                    Productos_de_Peticion.objects.create(
                        id_peticion=Peticion_Creada,
                        id_producto=Producto.objects.get(id=productos[i]),
                        calidad=calidad[i],
                        cantidad=cantidad[i])
                    print(i)




                return redirect('peticiones:PeticionListar')
                #print("entramos aqui en POST")
                #orden = form.save()
                #orden_creada = orden.save(commit=False)
                #print("ORDEN CREADA:",orden_creada)
                #print(orden_creada.id)
                #print(orden_creada.observacion)
                #orden_creada.save()
            
                #print(suministro.cleaned_data)

                
            #    contexto = {'user': request.user,
            #                }
                
            
            
            
            else:

                print("la orden no fue creada...")
                
            # redirect to a new URL:
            return render(request, 'peticiones/peticiones-crear.html',contexto)
    
    
    
    
    #Si el usuario no esta autenticado
    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')


    #print(contexto)
    return render(request, 'peticiones/peticiones-crear.html', contexto)







"""
class PeticionCrear(CreateView):

    model = Peticion  
    #form_class = PeticionPersonalizadoForm
    template_name = "peticiones/peticiones-crear.html"
    success_url = reverse_lazy('peticiones:PeticionListar')

    
    #Para enviar argumentos al formulario
    #def get_form_kwargs(self):
        #kwargs = super(PeticionPersonalizadoForm, self).get_form_kwargs()
        #kwargs['usuario'] = self.request.user
    #    return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Petición"
        return context

    def post(self,request,*args,**kwargs):
        
        print("entrando en post")

        #Si pide argumentos se lo pasamos
        form = PeticionPersonalizadoForm(data=request.POST)#,usuario=self.request.user
        if form.is_valid():
            form.save()#Guardamos el objeto
            return HttpResponseRedirect(self.success_url)

        #En caso de que no se cree el self.object se coloca en None
        self.object = None
        print(form.errors)

        #Aqui llamamos a todas las variables establecidas en get_context
        context = self.get_context_data(**kwargs)
        context['form'] = form

        #Asi es otra forma de enviar el contexto
        return render(request,self.template_name,context)
        
        #Asi es una forma de enviar
        #return render(request,self.template_name,{"form":form})
"""


class Peticionlistar(ListView):

    model = Peticion  
    #form_class = ProductoForm
    context_object_name = 'peticiones'
    template_name = "peticiones/peticiones-listar.html"
    success_url = reverse_lazy('base_principal:index')
    #queryset = Peticion.objects.filter(cliente=request.user) #Esta es una forma


    #Para establecer parametros en context_object_name
    def get_queryset(self):


        #Aqui debemos hacer una logica en caso de que sea administrador o usuario diferente a administrador
        print("Usuario Perfil:",self.request.user.rol)
        if self.request.user.rol == "administrador":
            return Peticion.objects.all() # Get 5 books containing the title war
        else:
            return Peticion.objects.filter(cliente=self.request.user) # Get 5 books containing the title war
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context







class Peticion_Productos_View(ListView):
    model = Productos_de_Peticion
    context_object_name = "Productos"
    template_name = "peticiones/peticiones-productos.html"

    #Para establecer parametros en context_object_name
    def get_queryset(self):

        #Aqui debemos hacer una logica en caso de que sea administrador o usuario diferente a administrador
        print("Usuario Perfil:",self.request.user.rol,"Variable: ",self.kwargs.get('pk',None))
        return Productos_de_Peticion.objects.filter(id_peticion=self.kwargs.get('pk',None)) # Get 5 books containing the title war
    



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print("jajajaja detalles empresa de : ",self.object.id)
        #print(Departamento.objects.filter(empresa_id=self.object.id))
        context['id'] = self.kwargs.get('pk',None)
        context['titulo'] = "Detail Company"
        #context['departamentos'] = Departamento.objects.filter(empresa_id=self.object.id).order_by("-fecha_creacion")
        #context['cantidad_empresas'] = Empresa.objects.filter(creado_por=self.request.user.id).count()
        context['usuario'] = self.request.user
        #context['entrevista_lista'] = Entrevista.objects.filter(departamento_id=self.object.id)
        return context



class Peticion_Procesos_View(DetailView):
    
    model = Peticion
    context_object_name = "peticion"
    template_name = "peticiones/peticiones-procesos.html"

    #Para establecer parametros en context_object_name
    #def get_queryset(self):

        #Aqui debemos hacer una logica en caso de que sea administrador o usuario diferente a administrador
    #    print("Usuario Perfil:",self.request.user.rol,"Variable: ",self.kwargs.get('pk',None))
    #    return Productos_de_Peticion.objects.filter(id_peticion=self.kwargs.get('pk',None)) # Get 5 books containing the title war
    

    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("jajajaja detalles peticion de : ",self.object.id)
        context['id'] = self.kwargs.get('pk',None)
        #context['titulo'] = "Detail Company"
        context['usuario'] = self.request.user
        #context['entrevista_lista'] = Entrevista.objects.filter(departamento_id=self.object.id)
        return context



#############################################################################################





###### Para aprobar las peticiones ########

def Peticion_Aprobar(request,pk):
    #verificamos que estamos ogeados
    if request.user.is_authenticated:
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("ENTRAMOS EN GET PARA APROBAR LA PETICION",pk)

            #Aqui hacemos todo lo que se necesita para aprobar
            Peticion_aprobar = Peticion.objects.get(id=pk)
            Peticion_aprobar.revision = True
            print(Usuarios.objects.get(id=request.user.id))
            Peticion_aprobar.aprobado_por = Usuarios.objects.get(id=request.user.id)
            Peticion_aprobar.oferta = True
            Peticion_aprobar.estado_peticion = "oferta"
            Peticion_aprobar.save()

            print(Peticion_aprobar)
            
            #contexto = {'form': form,
            #            'user': request.user}
            #print("entramos en GET:", orden)
            # redirect to a new URL:
            return redirect('peticiones:PeticionListar')






        #Metodo(POST)
        else:

            #print(request.POST)
            print("\nEntramos en POST de la peticionAPROBAR\n")
            print(request.POST)
            

            #Variables para guardar
            #productos = request.POST.getlist('productos')
            #calidad = request.POST.getlist('calidad')
            #cantidad = request.POST.getlist('cantidad')
            
            #print(productos," jajajajaja")

            #si el formulario tiene los datos correctos entramos aqui
            
            return redirect('peticiones:PeticionListar')
            
            
    
    
    
    
    #Si el usuario no esta autenticado
    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')

