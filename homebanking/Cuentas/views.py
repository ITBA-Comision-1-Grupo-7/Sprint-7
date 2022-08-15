from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
# Create your views here.

def Cuenta(request):
    return render(request,"cuentas/cuentas.html")
