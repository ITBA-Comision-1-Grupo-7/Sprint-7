from django import forms 
from .models import Prestamos 

class createPrestamo(forms.ModelForm):
  class Meta:
    model = Prestamos
    fields = '__all__'
