from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import loginForm

def login(request):
    return render(request, "login/login.html")


def loginform(request):
    login_form = loginForm
    if request.method == "POST":
        #Traemos los datos enviados
        login_form = login_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if login_form.is_valid():
            name = request.POST.get('name','')
            password = request.POST.get('password','')
            return render(request,'login/login.html',{'enviado': name}) 
    return render(request, "login/login.html", {'form':login_form})
