from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario
from django.http import HttpResponseRedirect
from ..form import Newusr, Login
from django.contrib.auth import authenticate, login


def inicio_sesion(request):
    pass


def usuario_nuevo(request):
    pass
    # new_usr = Newusr(request.POST or None)
    #
    # variables = {
    #     "new": new_usr,
    # }
    #
    # if new_usr.is_valid():
    #     datos = new_usr.cleaned_data
    #     nombre = datos.get("nombre")
    #     apellido = datos.get("apellidos")
    #     nombreusuario = datos.get("nombreUsuario")
    #     password = datos.get("password")
    #     telefono = datos.get("telefono")
    #     email = datos.get("email")
    #     db_register = Usuario(nombre=nombre, apellidos=apellido, nombreUsuario=nombreusuario,
    #                           password=password, telefono=telefono, email=email)
    #     db_register.full_clean()
    #     db_register.save()
    # return render(request, 'login/crear.html', variables)
