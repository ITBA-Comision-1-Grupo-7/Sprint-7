from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Cliente
from login.form import RegistroForm
import sqlite3

# Create your views here.


def Cuenta(request):
    # form = RegistroForm
    
    print(request.user)
    
    # print(form.fields['cliente_id'])
    
    # miCliente = Cliente

    # miCliente.dni = form.cleaned_data['cliente_id']
    
    # print(miCliente.dni)
    # miCliente = Cliente()
    # print(RegistroForm.email)

    # miCliente.dni = RegistroForm.cliente_id
    
    
    # miCliente.img='classic.png'

    # sqliteconnection = sqlite3.connect('db.sqlite3')

    # cursor = sqliteconnection.cursor()
    # cursor.execute('SELECT customer_name FROM cliente WHERE customer_DNI =' + miCliente.dni)
    # miCliente.nombre = cursor.fetchall()
    # miCliente.nombre = str(miCliente.nombre[0][0])
    # cursor.execute('SELECT customer_surname FROM cliente WHERE customer_DNI =' + Cliente.dni)
    # miCliente.apellido = cursor.fetchall()
    # miCliente.apellido = str(miCliente.apellido[0][0])
    # cursor.execute('SELECT customer_id FROM cliente WHERE customer_DNI =' + miCliente.dni)
    # miCliente.idCuenta = cursor.fetchall()
    # miCliente.idCuenta = str(miCliente.idCuenta[0][0])
    # cursor.execute('SELECT balance FROM cuenta WHERE customer_id =' + miCliente.idCuenta)
    # miCliente.balance = cursor.fetchall()
    # miCliente.balance = str(miCliente.balance[0][0])
    # cursor.execute('SELECT account_type_id FROM cuenta WHERE customer_id =' + miCliente.idCuenta)
    # miCliente.tipoCuenta = cursor.fetchall()
    # miCliente.tipoCuenta = str(miCliente.tipoCuenta[0][0])
    # cursor.execute('SELECT card_number FROM tarjetas WHERE card_id =' + miCliente.idCuenta)
    # miCliente.tarjeta = cursor.fetchall()
    # miCliente.tarjetaUlt = str(miCliente.tarjeta[0][0])

    # Cliente.tarjetaUlt = Cliente.tarjeta[-4:]

    # Cliente.balancef=float(Cliente.balance)
    # Cliente.balancef=(f"{Cliente.balancef:,.2f}")
    # Cliente.balancef=Cliente.balancef.replace(',',' ')
    # Cliente.balancef=Cliente.balancef.replace('.',',')

    # if Cliente.tipoCuenta == '1':
    #     Cliente.tipoCuenta = 'Classic'
    #     Cliente.img='classic.png'
    # if Cliente.tipoCuenta == '2':
    #     Cliente.tipoCuenta = 'Gold'
    #     Cliente.img='gold.png'
    # if Cliente.tipoCuenta == '3':
    #     Cliente.tipoCuenta = 'Black'
    #     Cliente.img='black.png'
    # Cliente.nombreCompleto = Cliente.apellido + ', ' + Cliente.nombre

    # return render(request, "cuentas/cuentas.html", {'Cliente': miCliente})
