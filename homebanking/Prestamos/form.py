from django import forms 
from .models import Prestamos 
import datetime

class createPrestamo(forms.Form):
    nombre = forms.CharField(label="Nombre", required=False)
    apellido =forms.CharField(label="Apellido", required= True)
    fecha_inicio = forms.DateField(initial=datetime.date.today, widget = forms.HiddenInput())
    PRESTAMO_PERSONAL = "PP"
    PRESTAMO_ESTUDIANTE = "PE"
    PRESTAMO_COMERCIOS = "PC"
    PRESTAMO_HIPOTECARIO= "PH"
    TIPO_PRESTAMO = [
      (PRESTAMO_PERSONAL,"Prestamo_personal"),
      (PRESTAMO_ESTUDIANTE,"Prestamo_estudiante"),
      (PRESTAMO_COMERCIOS,"Prestamo_comercios"),
      (PRESTAMO_HIPOTECARIO, "Prestamo_hipotecario"),
    ] 
    tipo_prestamo = forms.CharField(label='Tipo de prestamo',widget=forms.Select(choices=TIPO_PRESTAMO), initial=PRESTAMO_PERSONAL ,required=True)
    estado_prestamo= forms.BooleanField(label = 'estado', initial= True)
    
    # proyecto_id= forms.CharField(label='Que proyecto te intereso?', widget=forms.Select(choices=lista))