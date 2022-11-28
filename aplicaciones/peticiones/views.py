from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

#Aplicacion de PRODUCTOS
from aplicaciones.productos.models import Producto
from aplicaciones.productos.form import ProductoForm

#Aplicacion de PETICIONES
from aplicaciones.peticiones.models import Peticion
from aplicaciones.peticiones.form import PeticionPersonalizadoForm,PeticionForm




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
            #print("entramos en GET:", orden)






        #Metodo(POST)
        else:

            #print(request.POST)
            print("\nEntramos en post de la peticion")
            form = PeticionPersonalizadoForm(data=request.POST,usuario=request.user)

            #si el formulario tiene los datos correctos entramos aqui
            #if form.is_valid():
            # and trabajo.is_valid() and suministro.is_valid():
            
            
            #    print("\n")
            #    print("entramos aqui en POST")
                #orden = form.save()
                #orden_creada = orden.save(commit=False)
                #print("ORDEN CREADA:",orden_creada)
                #print(orden_creada.id)
                #print(orden_creada.observacion)
                #orden_creada.save()
            
                #print(suministro.cleaned_data)

                
            #    contexto = {'user': request.user,
            #                }
                
            
            
            
            #else:

            #    print("la orden no fue creada...")
                
            # redirect to a new URL:
            return render(request, 'servicios/ordenes/orden-creada.html',contexto)
    
    
    
    
    #Si el usuario no esta autenticado
    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')


    #print(contexto)
    return render(request, 'peticiones/peticiones-crear.html', contexto)


































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



#############################################################################################



