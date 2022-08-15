from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Cliente
import sqlite3
# Create your views here.

def Cuenta(request):
    #definitivamente no sé si funciona porque todo se rompe al no tener input
    #sqliteconnection=sqlite3.connect('db.sqlite3')
    #cursor=sqliteconnection.cursor()
    #cursor.execute('SELECT customer_name FROM cliente WHERE customer_DNI ='+ dni)
    # Cliente.nombre=cursor.fetchall()
    # Cliente.nombre=str(Cliente.nombre)
    # cursor.execute('SELECT customer_surname FROM cliente WHERE customer_DNI =' + dni)
    # Cliente.apellido=cursor.fetchall()
    # Cliente.apellido=str(Cliente.apellido)
    # cursor.execute('SELECT customer_id FROM cliente WHERE customer_DNI =' + dni)
    # Cliente.idCuenta=cursor.fetchall()
    # Cliente.idCuentastr(Cliente.idCuenta)
    # cursor.execute('SELECT balance FROM cuenta WHERE customer_id =' + customer_id)
    # Cliente.balance=cursor.fetchall()
    # Cliente.balance=str(Cliente.balance)
    # cursor.execute('SELECT account_type_id FROM cuenta WHERE customer_id =' + customer_id)
    # Cliente.tipoCuenta=cursor.fetchall()
    # Cliente.tipoCuenta=str(Cliente.tipoCuenta)

    # if Cliente.tipoCuenta==1:
    #     Cliente.tipoCuenta='Classic'
    # if Cliente.tipoCuenta==2:
    #     Cliente.tipoCuenta='Gold' 
    # if Cliente.tipoCuenta==3:
    #     Cliente.tipoCuenta='Black'
    return render(request,"cuentas/cuentas.html",{'Cliente':Cliente})
