from django import forms
from .models import Categoria


class Newusr(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput, required=True)
    apellidos = forms.CharField(widget=forms.TextInput, required=True)
    nombreUsuario = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.TextInput, required=True)
    telefono = forms.CharField(widget=forms.TextInput, required=True)
    email = forms.EmailField(widget=forms.TextInput, required=True)


class Login(forms.Form):
    nombreUsuario = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.TextInput, required=True)

class Categoria(forms.Form):
    class Meta:
        model = Categoria
        fields = ['nombre','img','descripcion']
