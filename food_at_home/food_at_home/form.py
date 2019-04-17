from django import forms


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


class FormCategoria(forms.Form):
    # nombre = forms.CharField(widget=forms.TextInput, required=True)
    # descripcion = forms.CharField(widget=forms.TextInput, required=True)
    img = forms.ImageField()
