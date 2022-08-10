from django import forms

class TarjetaForm(forms.Form):
    name = forms.CharField(label="Nombre completo", required=True)
    email = forms.EmailField(label="Email", required=True)
    lista=[('3','Debito Classic'),  ('4','Credit Gold'), ('5', 'Credit Black')]
    tarjeta_id= forms.CharField(label='¿Que tipo de tarjeta desea?', widget=forms.Select(choices=lista))