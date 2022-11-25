from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group



#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

    



class Index(TemplateView):

    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("Permisos: ",list(Permission.objects.all()))
            print("usuario: ",request.user," Cantidad de Grupos: ",Group.objects.all().count())

            #GCliente = Group.objects.get(name="cliente_E")

            print("\n\n")
            #print("\n\nPermisos Grupo Productor: ",GProductor.permissions.all() )
            #for elemento in GCliente.permissions.all():
            #    print(elemento.name)
            #print("\n\n")

            #Grupo_productor.permissions.set(Permission.objects.get(name="Can add inventario"),
            print("administrador:",request.user.groups.filter(name='administrador').exists())
            print("productor:",request.user.groups.filter(name='productor').exists())
            print("cliente Externo:",request.user.groups.filter(name='cliente_E').exists())
            print("cliente Interno:",request.user.groups.filter(name='cliente_I').exists())
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

