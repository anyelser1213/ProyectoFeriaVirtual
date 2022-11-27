"""sitioWeb URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

#from inventario_stock.views import views as vistasInventarioStock


app_name="ventas"


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('aplicaciones.base_principal.urls'))),
    path('', include(('aplicaciones.peticiones.urls'))),
    path('', include(('aplicaciones.inventario_stock.urls'))),
    path('', include(('aplicaciones.usuarios.urls'))),
    path('', include(('aplicaciones.login.urls'))),
    #path('logout/', vistaLogin.Logout.as_view() ,name="logout"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)