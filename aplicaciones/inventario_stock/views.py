from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from aplicaciones.inventario_stock.form import * #CalidadForm
from aplicaciones.inventario_stock.models import *

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

from django.urls import reverse, reverse_lazy

from aplicaciones.usuarios.form import NewUserForm


# Create your views here.


class ProductosCrear(CreateView):

    model = Producto  
    form_class = ProductoForm
    template_name = "inventario_stock/productos/productos-crear.html"
    success_url = reverse_lazy('inventario_stock:ProductoListar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Productos"
        context['usuario'] = self.request.user
        return context

    def post(self,request,*args,**kwargs):
        
        print("entrando en post")

        form = ProductoForm(request.POST)
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


class Productoslistar(ListView):

    model = Producto  
    #form_class = ProductoForm
    context_object_name = 'productos'
    template_name = "inventario_stock/productos/productos-listar.html"
    success_url = reverse_lazy('base_principal:index')



class ProductosCrear(CreateView):

    model = Producto  
    form_class = ProductoForm
    template_name = "inventario_stock/productos/productos-crear.html"
    success_url = reverse_lazy('inventario_stock:ProductoListar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Productos"
        context['usuario'] = self.request.user
        return context

    def post(self,request,*args,**kwargs):
        
        print("entrando en post")

        form = ProductoForm(request.POST)
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



"""
class Inventario_asignar(TemplateView):

    template_name = "inventario_stock/inventario/inventario-crear.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("usuario permisos: ",request.user.get_all_permissions())
            #Aqui verificamos si el usuario esta activo para que ingrese
            ''' 
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
            '''


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        #context['informacion'] = "Hola..."

       
        context['usuario'] = self.request.user
        return context
"""



#Vista basada en funciones que usaremos despues
"""

def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request, 'form_template.html', {'form': form})


"""