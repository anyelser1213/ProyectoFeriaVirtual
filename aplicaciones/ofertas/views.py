from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

#Aplicacion de PRODUCTOS
from aplicaciones.productos.models import Producto
from aplicaciones.productos.form import ProductoForm

#Aplicacion de PETICIONES
from aplicaciones.peticiones.models import Peticion
from aplicaciones.peticiones.form import PeticionForm



from aplicaciones.ofertas.models import Contrato






#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

# Create your views here.





################### PARA OFERTAS NACIONALES E INTERNACIONALES ########################


class Ofertas_Nacionales(TemplateView):

    template_name = "inventario_stock/ofertas/nacionales.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("Permisos: ",list(Permission.objects.all()))
            print("usuario: ",request.user)

            #Grupo_productor.permissions.set(Permission.objects.get(name="Can add inventario"),
            print("administrador:",request.user.groups.filter(name='administrador').exists())
            print("productor:",request.user.groups.filter(name='productor').exists())
            print("cliente :",request.user.groups.filter(name='cliente').exists())
            print("\n\n")
            #print("usuario permisos: ",request.user.get_all_permissions())
            #print(request.user.has_perm('src.ver_zulia'))
            #print("uSUARIO : ",request.user.has_module_perms())
            
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
        context['informacion'] = "Hola..."

        context['ofertas'] = Peticion.objects.none()
        context['contrato'] ="SIN CONTRATO"
        #Aqui verificamos si el inventario ya existe
        contrato_usuario = Contrato.objects.filter(usuario=self.request.user)
        if contrato_usuario.exists():
            print("Si tiene contrato")
            
            #Verificamos si tiene el contrato vigente
            contrato_vigente = Contrato.objects.get(usuario=self.request.user)
            if contrato_vigente.estado_contrato == "vigente":
                print("El contrato del usuario:",self.request.user.username,"SI esta vigente.")
                context['ofertas'] = Peticion.objects.filter(tipo_peticion="nacional")
                context['contrato'] ="CONTRATO VIGENTE"

            else:
                print("El contrato del usuario:",self.request.user.username,"NO esta vigente.")
                context['ofertas'] = Peticion.objects.none()
                context['contrato'] ="CONTRATO CADUCADO"
        else:
            print("No tiene contrato")
            context['contrato'] ="SIN CONTRATO"
        
        return context


class Ofertas_Internacionales(TemplateView):

    template_name = "inventario_stock/ofertas/internacionales.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("Permisos: ",list(Permission.objects.all()))
            print("usuario: ",request.user)

            #Grupo_productor.permissions.set(Permission.objects.get(name="Can add inventario"),
            print("administrador:",request.user.groups.filter(name='administrador').exists())
            print("productor:",request.user.groups.filter(name='productor').exists())
            print("cliente :",request.user.groups.filter(name='cliente').exists())
            print("\n\n")
            #print("usuario permisos: ",request.user.get_all_permissions())
            #print(request.user.has_perm('src.ver_zulia'))
            #print("uSUARIO : ",request.user.has_module_perms())
            
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
        context['informacion'] = "Hola..."

        context['ofertas'] = Peticion.objects.none()
        context['contrato'] ="SIN CONTRATO"
        #Aqui verificamos si el inventario ya existe
        contrato_usuario = Contrato.objects.filter(usuario=self.request.user)
        if contrato_usuario.exists():
            print("Si tiene contrato")
            
            #Verificamos si tiene el contrato vigente
            contrato_vigente = Contrato.objects.get(usuario=self.request.user)
            if contrato_vigente.estado_contrato == "vigente":
                print("El contrato del usuario:",self.request.user.username,"SI esta vigente.")
                context['ofertas'] = Peticion.objects.filter(tipo_peticion="internacional")
                context['contrato'] ="CONTRATO VIGENTE"

            else:
                print("El contrato del usuario:",self.request.user.username,"NO esta vigente.")
                context['ofertas'] = Peticion.objects.none()
                context['contrato'] ="CONTRATO CADUCADO"
        else:
            print("No tiene contrato")
            context['contrato'] ="SIN CONTRATO"
        
        return context



######################################################################################
