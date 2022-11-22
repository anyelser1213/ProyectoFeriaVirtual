from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from aplicaciones.inventario_stock.form import CalidadForm
from aplicaciones.inventario_stock.models import Calidad

from django.urls import reverse, reverse_lazy


# Create your views here.


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