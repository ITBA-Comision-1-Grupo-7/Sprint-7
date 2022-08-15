from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Cliente
from login.forms import loginForm
import sqlite3
# Create your views here.

def Cuenta(request):
    # definitivamente no sé si funciona porque todo se rompe al no tener input
      Cliente.dni=loginForm.name

      sqliteconnection=sqlite3.connect('db.sqlite3')
    
      cursor=sqliteconnection.cursor()
      cursor.execute('SELECT customer_name FROM cliente WHERE customer_DNI ='+ Cliente.dni)
      Cliente.nombre=cursor.fetchall()
      Cliente.nombre=str(Cliente.nombre[0][0])
      cursor.execute('SELECT customer_surname FROM cliente WHERE customer_DNI =' + Cliente.dni)
      Cliente.apellido=cursor.fetchall()
      Cliente.apellido=str(Cliente.apellido[0][0])
      cursor.execute('SELECT customer_id FROM cliente WHERE customer_DNI =' + Cliente.dni)
      Cliente.idCuenta=cursor.fetchall()
      Cliente.idCuenta=str(Cliente.idCuenta[0][0])
      cursor.execute('SELECT balance FROM cuenta WHERE customer_id =' + Cliente.idCuenta)
      Cliente.balance=cursor.fetchall()
      Cliente.balance=str(Cliente.balance[0][0])
      cursor.execute('SELECT account_type_id FROM cuenta WHERE customer_id =' + Cliente.idCuenta)
      Cliente.tipoCuenta=cursor.fetchall()
      Cliente.tipoCuenta=str(Cliente.tipoCuenta[0][0])
      cursor.execute('SELECT card_number FROM tarjetas WHERE card_id =' +Cliente.idCuenta)
      Cliente.tarjeta=cursor.fetchall()
      Cliente.tarjetaUlt=str(Cliente.tarjeta[0][0])

      Cliente.tarjetaUlt=Cliente.tarjeta[-4:]

      if Cliente.tipoCuenta=='1':
          Cliente.tipoCuenta='Classic'
      if Cliente.tipoCuenta=='2':
          Cliente.tipoCuenta='Gold' 
      if Cliente.tipoCuenta=='3':
          Cliente.tipoCuenta='Black'
      Cliente.nombreCompleto=Cliente.apellido + ', ' + Cliente.nombre

      return render(request,"cuentas/cuentas.html",{'Cliente':Cliente})
