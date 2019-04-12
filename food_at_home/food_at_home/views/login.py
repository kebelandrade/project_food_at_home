from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario
from django.http import HttpResponseRedirect
from ..form import Newusr, Login
from django.contrib.auth import authenticate, login


def inicio_sesion(request):
    login_user = Login(request.POST or None)

    if login_user.is_valid():
        data = login_user.cleaned_data
        usuario = data.get("nombreUsuario")
        password = data.get("password")
        print(usuario)
        print(password)
        acceso = authenticate(username=usuario, password=password)
        if acceso is not None:
            login(request, acceso)
            return HttpResponseRedirect("Entró")
        else:
            return HttpResponseRedirect("Usuario / Contraseña Incorrecto")

    else:
        login_user = Login()

    log = {
        "login_user": login_user,
    }

    return render(request, 'login/mostrar.html', log)


def usuario_nuevo(request):
    new_usr = Newusr(request.POST or None)

    variables = {
        "new": new_usr,
    }

    if new_usr.is_valid():
        datos = new_usr.cleaned_data
        nombre = datos.get("nombre")
        apellido = datos.get("apellidos")
        nombreusuario = datos.get("nombreUsuario")
        password = datos.get("password")
        telefono = datos.get("telefono")
        email = datos.get("email")
        db_register = Usuario(nombre=nombre, apellidos=apellido, nombreUsuario=nombreusuario,
                              password=password, telefono=telefono, email=email)
        db_register.full_clean()
        db_register.save()
    return render(request, 'login/crear.html', variables)

