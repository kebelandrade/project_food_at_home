from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import *
from django.template.response import *
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import messages

#
# def login(request):
#     return render(request, 'login/login.html')


def form(request):
    return render(request, 'formulario.html')


def iniciousuario(request):
    return render(request, 'cliente/inicio_usuario_cliente.html')


def guardar_user(req):
    # if request.is_ajax:
    #     r_nombre = request.GET.get('nombre')
    #     r_apellidos= request.GET.get('apellido')
    #     r_nombreUsuario = request.GET.get('usuario')
    #     r_password = request.GET.get('contrasena')
    #     r_telefono = request.GET.get('telefono')
    #     r_email = request.GET.get('email')
    #
    #     usuario =Usuario()
    #     # # nombre.Nombre.objects.GET(pk=nombre)
    #     # # apellidos.Apellido.objects.GET(pk=apellidos)
    #     # # nombreUsuario.NombreUsuario.objects.GET(pk=nombreUsuario)
    #     # # password.Password.objects.GET(pk=password)
    #     # # telefono.Telefono.objects.GET(pk=telefono)
    #     # # email.Email.objects.GET(pk=email)
    #     #
    #     usuario.nombre=r_nombre
    #     usuario.apellidos=r_apellidos
    #     usuario.nombreUsuario=r_nombreUsuario
    #     usuario.password=r_password
    #     usuario.telefono=r_telefono
    #     usuario.email=r_email
    #
    #     usuario.save()
    #
    #     data = 'se guardo el mensaje'
    # else:
    #     data = 'Fallo'
    #
    # return render(data, 'index.')
    errores = []
    exito = True
    valor = 2;
    try:
        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = req.POST.get('nombre', None)
        nuevo_usuario.apellidos = req.POST.get('apellido', None)
        nuevo_usuario.nombreUsuario = req.POST.get('usuario', None)
        nuevo_usuario.password = req.POST.get('contrasena', None)
        nuevo_usuario.telefono = req.POST.get('telefono', None)
        nuevo_usuario.email = req.POST.get('email', None)
        nuevo_usuario.tipoUsuario = valor
        nuevo_usuario.full_clean()
        nuevo_usuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False

    if exito:
        return render(req,'login/agradecimiento.html')
    elif not exito:
        return JsonResponse({
            'exito': exito,
            'errores': errores
        })


def configuracion(request):
    return render(request, 'cliente/configuracion_cliente.html')


def usuario_nuevo(request):
    # new_usr = Usuario()
    return render(request, 'login/Usuario_Nuevo.html')


def crear_usuario(req):
    errores = []
    exito = True
    try:
        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = req.POST.get('nombre', None)
        nuevo_usuario.apellidos = req.POST.get('apellido', None)
        nuevo_usuario.nombreUsuario = req.POST.get('nombreUsuario', None)
        nuevo_usuario.password = req.POST.get("password", None)
        nuevo_usuario.email = req.POST.get("email", None)
        nuevo_usuario.full_clean()
        nuevo_usuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_usuario(req, id):
    errores = []
    exito = True
    try:
        usuario = Usuario.objects.filter(id=id).first()
        usuario.nombre = req.POST.get('nombre', '')
        usuario.apellidos = req.POST.get('apellido', '')
        usuario.nombreUsuario = req.POST.get('nombreUsuario', '')
        usuario.password = req.POST.get("password", '')
        usuario.email = req.POST.get("email", '')
        usuario.full_clean()
        usuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def user(request, name):
    usuario = Usuario.objects.filter(nombreUsuario = name)
    ciudades = Ciudad.objects.all()
    restaurante = Restaurante.objects.all()
    direccion = DireccionRestaurante.objects.values('ciudad_id', 'restaurante_id').distinct()
    return TemplateResponse(request, 'cliente/inicio_usuario_cliente.html', {'ciudades':ciudades,
                                                                             'restaurante':restaurante,
                                                                             'direccion': direccion,
                                                                             'usuario': usuario})


def eliminar_usuario(req):
    pass
