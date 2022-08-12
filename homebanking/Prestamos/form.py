from django import forms 
from .models import Prestamos 
import datetime

class createPrestamo(forms.Form):
    dni = forms.CharField(label="DNI", required=True)
    apellido =forms.CharField(label="Apellido", required= True)
    fecha_inicio = forms.DateField(initial=datetime.date.today, widget = forms.HiddenInput())
    PRESTAMO_PERSONAL = "PP"
    PRESTAMO_ESTUDIANTE = "PE"
    PRESTAMO_COMERCIOS = "PC"
    PRESTAMO_HIPOTECARIO= "PH"
    TIPO_PRESTAMO = [
      (PRESTAMO_PERSONAL,"Prestamo_Personal"),
      (PRESTAMO_ESTUDIANTE,"Prestamo_Estudiante"),
      (PRESTAMO_COMERCIOS,"Prestamo_Comercios"),
      (PRESTAMO_HIPOTECARIO, "Prestamo_Hipotecario"),
    ] 
    valor = forms.CharField(label='Valor del prestamo', initial=0, required= True)
    tipo_prestamo = forms.CharField(label='Tipo de prestamo',widget=forms.Select(choices=TIPO_PRESTAMO), initial=PRESTAMO_PERSONAL ,required=True)
    estado_prestamo= forms.BooleanField(label = 'Estado', initial= True)
    