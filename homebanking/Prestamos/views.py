from django.shortcuts import render
from .form import createPrestamo
from .models import Prestamos
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

#usamos el decorador
# @login_required
def prestamo(request):
    contact_form = createPrestamo
    if request.method == "POST":
        #Traemos los datos enviados
        contact_form = contact_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if contact_form.is_valid():
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            fecha_inicio = request.POST.get('fecha_inicio')
            tipo_prestamo = request.POST.get('tipo_prestamo')
            estado = request.POST.get('estado_prestamo')
            prestamo = Prestamos(nombre= nombre, apellido= apellido ,fecha_inicio= fecha_inicio, tipo_prestamo=tipo_prestamo,estado_prestamo= estado)
            prestamo.save()
            return render(request,'prestamos/prestamos.html',{'enviado': apellido})   
    return render(request,'prestamos/prestamos.html',{'form': contact_form})