from django.shortcuts import render
from .form import createPrestamo
from django.views.generic.edit import CreateView 
from .models import Prestamos
# Create your views here.

class create_form_prestamos(CreateView):
    model = Prestamos 
    template_name = 'prestamos/prestamos.html'
    form_class = createPrestamo
