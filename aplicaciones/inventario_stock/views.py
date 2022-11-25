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

"""
class ProductosCrear(CreateView):


    template_name = "inventario_stock/productos/productos-crear.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            #print("usuario permisos: ",request.user.get_all_permissions())
            print("Estas autenticado GENIAL")
            #if request.user.has_perm('juegos.iniciarjugada'):
            print("Entramos en ProductosCrear")

                #jugada1 = Jugada.objects.first()
                #telefono1 = Telefono.objects.first()
                ##Jugadas_Numeros.objects.create()
                

            #else:

                #print("El usuario: ",request.user," no tiene acceso en CalidadCrear")
                #return redirect("principal:index")

            


            #print("usuario permisos: ",request.user.get_all_permissions())
            #print(request.user.has_perm('src.ver_zulia'))
            



            
            #Aqui verificamos si el usuario esta activo para que ingrese
            ''' 
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
            '''


            

            
            #empresa_creada = Empresa.objects.filter(creado_por_id=request.user.id)


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        #context['informacion'] = "Hola..."
        context['formProducto'] = ProductoForm()
        context['usuario'] = self.request.user.username
        return context

    def get_form_kwargs(self, *args, **kwargs):
        
        kwargs = super(ProductosCrear, self).get_form_kwargs(*args, **kwargs)
        #kwargs['user'] = self.request.user

        print("Pasamos por la funcion get_form_kwargs linea 251")
        return kwargs
    

    ############# METODO POST ############################
    def post(self, request, *args, **kwargs):

        print("Entramos en POST de ProductoCrear")
        print("\n\n")
        print(request.POST)
        print("\n\n")
        #print(request.FILES)
        print()
        #form = self.form_class(request.POST,request.FILES, user=self.request.user)
        form = ProductosCrear()

        if 1==1:
        #if form.is_valid():
        
        #    print("Fue valido la empresa...")
        
        #    producto = form.save()

        #    print("Este formulario de producto es valido")
            #titulosVideos = request.POST.getlist('titulo_video_empresa')
            #descripcionVideos = request.POST.getlist('descripcion_video_empresa')
            #listaVideosEmpresa = request.FILES.getlist('videos')#Para obtener una lista de sus valores
            






            contexto = {
                'fromProducto':ProductoForm()
            }

            #Aqui incluimos los otros contextos 
            #contexto.update(contextoVideoEmpresa)
            #contexto.update(contextoEquipoEmpresa)
            #contexto.update(contextoPremiosEmpresa)

            print("El contexto es: ", contexto)
            return render(request,"inventario_stock/productos/productos-crear.html",contexto)
            #return HttpResponseRedirect('/pruebas/')


        else:
            
            print("NO Fue valido la vaina...")
                    
            contexto = {
                'fromProducto':ProductoForm()
            }

            #Para probar las cosas
            return render(request,"inventario_stock/productos/productos-crear.html",contexto)


"""

'''
class CalidadCrear(CreateView):

    model = Calidad  
    form_class = CalidadForm
    template_name = "inventario_stock/calidad/calidad-crear.html"
    success_url = reverse_lazy('base_principal:index')



class CalidadListar(ListView):
    model = Calidad
    queryset = Calidad.objects.all()
    context_object_name = 'calidad_lista'
    template_name = "inventario_stock/calidad/calidad-listar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Listar Calidad"
        context['usuario'] = self.request.user
        return context


'''




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