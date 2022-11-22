from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ="usuarios"

urlpatterns = [


    #path('', views.Index.as_view(), name='index'),
    
    #path('', views.index.as_view() ,name="index"),



    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)