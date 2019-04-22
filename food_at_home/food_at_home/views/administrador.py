from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario, Categoria
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import *
from django.template import *
from ..models import Empleado
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# from ..form import formCategoria
from django.contrib import messages


def index(request):
    email = request.POST.get('correo')
    password = request.POST.get('contra')
    error = 0
    # if request.method == 'POST':
    usuarios = Usuario.objects.all()
    if usuarios.email == email and usuarios.password == password:
        if usuarios.tipoUsuario == 1:
            return render(request, "administrador/root.html")
        elif usuarios.tipoUsuario == 2:
            return render(request, "cliente/inicio_usuario_cliente.html")
    else:
        messages.success(request, 'El correo o la contrasena son incorrectas')
        return render("login/login.html")
    # else:
    #     return render(request,"login/login.html")


    # return render(request, "administrador/root.html")



def gestion_usuarios(request):
    empleados = Empleado.objects.all()
    return TemplateResponse(request, 'administrador/Empleado.html', {'empleados': empleados})


def gestion_restaurante(request):
    return render(request, 'administrador/Restaurantes.html')


def gestion_ciudades(request):
    return render(request, 'administrador/ciudad.html')


def save_categoria(request):

    mensaje = []
    exito = True
    try:
        if request.method == 'POST':
        # form = formCategoria(request.POST, request.FILES)
            categorias = Categoria()
            categorias.nombre = request.POST.get('nombre', None)
            categorias.descripcion = request.POST.get('descripcion', None)
            categorias.img = request.FILES['img']
            # categorias.full_clean()
            categorias.save()
            exito = True
    except ValidationError as e:
        mensaje = e.messages
        exito = False
    if exito == True:
        messages.success(request, 'La categoria se ha creado correctamente')
        # return HttpResponse('administrador/Restaurantes.html')
        return render(request,'administrador/Restaurantes.html')
    elif exito == False:
        return HttpResponse('no')
