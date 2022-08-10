from django import forms
import datetime
class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre completo", required=True)
    email = forms.EmailField(label="Email", required=True)
    lista=[('3','Pesonales'),  ('4','Hipotecario'), ('5', 'Prendarios')]
    Fecha = forms.DateField(initial=datetime.date.today)
    proyecto_id= forms.CharField(label='¿Que tipo de prestamo desea?', widget=forms.Select(choices=lista))