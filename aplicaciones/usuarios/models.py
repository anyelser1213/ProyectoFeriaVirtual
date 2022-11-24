import os
import shutil #libreria para borrar carpetas esten o no llenas
from django.conf import settings
from django.db import models

#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete


# Create your models here.

##################################################################################################
####################### Modelos para Usuarios ####################################################


class UsuarioManager(BaseUserManager):

    def create_user(self,email,username,password=None,admin = False,is_superuser =False,rol="administrador"):
        print("Creamos Usuario Normal")
        #if not email:
        #    raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            
            username = username,
            email = self.normalize_email(email),
            password = password,
            rol = rol,
            admin =admin,
            is_superuser = is_superuser,
            #plan_elegido = plan_elegido,
        )

        #aqui encriptamos la clave para no guardar en texto plano
        print("ENCRIPTAMOS", password)
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    

    #Funcion para usuario administrador
    def create_superuser(self,email,username,password,rol="administrador",admin = True,is_superuser = True):
        print("Creamos superusuario")

        usuario = self.create_user(
            email = email,  
            username = username,
            rol = rol,
            password = password,
            admin =admin,
            is_superuser = is_superuser
        )
        
        print("Entramos en superuser")
        usuario.save()
        return usuario


#Funcion para agregar carpetas al usuario
def direccion_usuarios(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    print(instance)
    print(instance.id)
    print(instance.username)
    return 'usuarios/fondos/{0}/{1}'.format(instance.username, filename)

"""
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
         return str(self.nombre)

    class Meta:

        verbose_name = "Rol"
        verbose_name_plural = "Roles"

        permissions = [
            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos


"""



# Heredamos de AbstractBaseUser para adaptarlo a nuestro gusto
class Usuarios(AbstractBaseUser,PermissionsMixin):

    #(Lo que se guarda en bases de datos, lo que se ve al usuario)
    rol = [
        
        ('master','Master'),
        ('administrador','Administrador'),
        ('productor','Productor'),
        ('cliente_E','Cliente Externo'),
        ('cliente_I','Cliente Interno'),
        ('transportista','transportista'),
        ('consultor','consultor'),
    ]

    #tipo_plan = [
    #    ('gratis','Free'),
    #    ('pago','Pay'),
    #]
    
    id = models.AutoField(primary_key=True)
    username = models.CharField("Username",max_length=200,unique=True)
    nombres = models.CharField("Nombres",max_length=200,blank=True, null=True) 
    apellidos = models.CharField("Apellidos",max_length=200,blank=True, null=True) 
    email = models.EmailField("Correo Electronico",max_length=150, unique=True)
    #empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True)
    activo = models.BooleanField(default=True)#Para poder ingresar al sistema  
    is_superuser = models.BooleanField(default=False)#Este es superusuario
    admin = models.BooleanField(default=False)#Para poder ingresar al admin de django
    cedula = models.IntegerField(default=0,blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    ultimo_ingreso = models.DateTimeField('actualizado', auto_now=True)
    direccion = models.CharField("Direccion",max_length=100,blank=True, null=True,default="Las Adjuntas") 
     
    rol = models.CharField("Rol",max_length=150,choices=rol,default='cliente',blank=True, null=True)
    #rol = models.ForeignKey(Rol,on_delete=models.CASCADE,blank=False, null=True)
    #rol = models.CharField("Rol",max_length=150,choices=usuario_tipos,default='cliente',blank=True, null=True)

    #plan_elegido = models.CharField("Plan",
    #    max_length=150,
    #    choices=tipo_plan,    
    #    default='libre'
    #)

    telefono = models.CharField("Telefono", max_length=50,blank=True,null=True,default="04242020470")
    #imagenFondoEscritorio = models.ImageField("Imagen de Escritorio", upload_to=direccion_usuarios, max_length=200,blank=True,null=True)
    
    #Para enlazar al manager que has creado
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'  #Para estableccer este campo como unico
    REQUIRED_FIELDS = ['email','is_superuser'] # Campos obligatorios(los pide cuando los creas por consola)

    def __str__(self):
        return f'Usuario {self.username}'
    
    
    
    #para verificar si un usuario es administrador o no(Para entrar en el admin)
    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         if self.activo:
            return self.admin
         return False
     

    def has_module_perms(self, app_label):
        return True

    

################# AQUI HACEMOS TODAS LAS PRUEBAS #########################




    def save(self, *args, **kwargs):
        
        super(Usuarios, self).save(*args, **kwargs)
        
        
        
        print(self.id,"Guardamos al loco : ", self.rol)

        migrupo = ""
        #Vamos a probar
        if Group.objects.all().count() >0:

            print("Ya existen los grupos\n\n")
            migrupo = Group.objects.get(name=str(self.rol))
            self.groups.add(migrupo)
            #self.groups.add(migrupo)

        else:

            print("Vamos a crear a los grupos")

            Grupo_administrador = Group.objects.create(name="administrador")
            Grupo_productor = Group.objects.create(name="productor") #Permisos solo para productor
            Grupo_cliente = Group.objects.create(name="cliente") #Permisos solo para cliente


            Grupo_administrador.permissions.set(list(Permission.objects.all())) #Todos los permisos
            Grupo_productor.permissions.add(
                                Permission.objects.get(name="Can add inventario"),
                                Permission.objects.get(name="Can change inventario"),
                                Permission.objects.get(name="Can delete inventario"),
                                Permission.objects.get(name="Can view inventario"),
                                Permission.objects.get(name="Can add producto"),
                                Permission.objects.get(name="Can change producto"),
                                Permission.objects.get(name="Can delete producto"),
                                Permission.objects.get(name="Can view producto"),
            )
            

            #Grupo_administrador.permissions.add(permiso1, permiso2, ...)
            #self.groups.add(Grupo_administrador)

            migrupo = Group.objects.get(name=str(self.rol))
            self.groups.add(migrupo)
            #self.per.add(migrupo)






        print("Gruepo asignado: ",migrupo," Permisos:",self.get_group_permissions())



    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
            
            
            
            
            
            
        ]#Fin de los permisos




    


##########################################################################################################
##########################################################################################################

