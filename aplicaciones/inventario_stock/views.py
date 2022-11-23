from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from aplicaciones.inventario_stock.form import * #CalidadForm
from aplicaciones.inventario_stock.models import *

#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

from django.urls import reverse, reverse_lazy

from aplicaciones.usuarios.form import NewUserForm


# Create your views here.


class ProductoresCrear(TemplateView):

    template_name = "inventario_stock/productores/productores-crear.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            #print("usuario permisos: ",request.user.get_all_permissions())
            print("Estas autenticado GENIAL")
            #if request.user.has_perm('juegos.iniciarjugada'):
            print("Entramos en CalidadCrear")

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

            #return redirect("src:index")
            #print("Usuario ",request.user)

            #Esto es algo que podria funcionar en algun momento
            #grupo="prueba"
            #print('Proyecto %s' % (grupo))

            

            
            #empresa_creada = Empresa.objects.filter(creado_por_id=request.user.id)


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        #context['informacion'] = "Hola..."
        context['formProductor'] = NewUserForm()
        context['usuario'] = self.request.user.username
        return context




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