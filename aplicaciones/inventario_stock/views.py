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





######################## PARA LAS PETICIONES ################################################


class PeticionCrear(CreateView):

    model = Peticion  
    form_class = PeticionForm
    template_name = "inventario_stock/peticiones/peticiones-crear.html"
    success_url = reverse_lazy('inventario_stock:PeticionListar')

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
    template_name = "inventario_stock/peticiones/peticiones-listar.html"
    success_url = reverse_lazy('base_principal:index')



#############################################################################################





#################### PARA INVENTARIO #############################

class Inventario_asignar(CreateView):

    model = Inventario  
    form_class = InventarioForm
    template_name = "inventario_stock/inventario/inventario-crear.html"
    success_url = reverse_lazy('inventario_stock:InventarioListar')

    #Para enviar argumentos al formulario
    def get_form_kwargs(self):
        kwargs = super(Inventario_asignar, self).get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Asignar Productos"
        context['usuario'] = self.request.user
        return context

    def post(self,request,*args,**kwargs):
        
        print("entrando en post con los datos:",request.POST)

        #Tomamos los datos de manera individual para ejecutar la logica
        productor = request.POST.get("productor_id")
        producto = request.POST.get("producto_id")
        cantidad = float(request.POST.get("cantidad"))
        calidad = request.POST.get("calidad")
        precio = float(request.POST.get("precio"))
        


        ###### Verificamos que existe en el inventario sino se crea uno nuevo ###

        #Aqui verificamos si el inventario ya existe
        inventario_actual = Inventario.objects.filter(productor_id=productor,producto_id=producto,calidad=calidad,tipo_peticion=tipo_peticion)
        if inventario_actual.exists():

            inventario_a_usar = Inventario.objects.get(productor_id=productor,producto_id=producto,calidad=calidad)
            inventario_a_usar.cantidad += cantidad 
            inventario_a_usar.precio = precio
            inventario_a_usar.save() 
            print("Inventario: ",inventario_a_usar)

            self.object = None
            context = self.get_context_data(**kwargs)
            context['inventarios'] = Inventario.objects.all()

            #Asi es otra forma de enviar el contexto
            return render(request,"inventario_stock/inventario/inventario-listar.html",context)
            
            
        else:
            pass


        print("El id del productor es: ", productor)


        form = ProductoForm(request.POST)
        if form.is_valid():
            #form.save()#Guardamos el objeto
            return HttpResponseRedirect(self.success_url)

        #En caso de que no se cree el self.object se coloca en None
        self.object = None
        print(form.errors)

        #Aqui llamamos a todas las variables establecidas en get_context
        context = self.get_context_data(**kwargs)
        context['form'] = form

        #Asi es otra forma de enviar el contexto
        return render(request,self.template_name,context)





class Inventariolistar(ListView):

    model = Inventario  
    #form_class = ProductoForm
    context_object_name = 'inventarios'
    template_name = "inventario_stock/inventario/inventario-listar.html"
    success_url = reverse_lazy('base_principal:index')




#######################################################################






























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