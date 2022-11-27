from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from aplicaciones.peticiones.models import Peticion
from aplicaciones.peticiones.form import * 

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

# Create your views here.



######################## PARA LAS PETICIONES ################################################


class PeticionCrear(CreateView):

    model = Peticion  
    form_class = PeticionForm
    template_name = "peticiones/peticiones-crear.html"
    success_url = reverse_lazy('peticiones:PeticionListar')

    #Para enviar argumentos al formulario
    def get_form_kwargs(self):
        kwargs = super(PeticionCrear, self).get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Petición"
        return context

    def post(self,request,*args,**kwargs):
        
        print("entrando en post")

        #Si pide argumentos se lo pasamos
        form = PeticionForm(request.POST,usuario=self.request.user)
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
