from django import forms
class loginForm(forms.Form):
    name = forms.CharField(label="Usuario o DNI", required=True)
    password = forms.CharField(widget=forms.PasswordInput())
