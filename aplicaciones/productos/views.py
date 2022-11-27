from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from aplicaciones.productos.form import ProductoForm
from aplicaciones.productos.models import Producto

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

from django.urls import reverse, reverse_lazy


# Create your views here.

#################### PARA PRODUCTOS #############################


class ProductosCrear(CreateView):

    model = Producto  
    form_class = ProductoForm
    template_name = "productos/productos-crear.html"
    success_url = reverse_lazy('productos:ProductoListar')

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
    template_name = "productos/productos-listar.html"
    success_url = reverse_lazy('base_principal:index')


