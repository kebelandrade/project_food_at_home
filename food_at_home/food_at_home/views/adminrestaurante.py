from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from ..models import *
from django.core import serializers
from django.template.response import *


def inicio_admin_res(request, name):
    usuario = Usuario.objects.filter(nombreUsuario=name)
    id_usuario = Usuario.objects.get(nombreUsuario=name)
    restaurante = Restaurante.objects.filter(usuario_id=id_usuario.id)
    ciudad = Ciudad.objects.all()
    categoria = Categoria.objects.all()
    return TemplateResponse(request, 'adminRes/index_admin_res.html', {'usuario': usuario,
                                                                       'res': restaurante,
                                                                       'ciudad': ciudad,
                                                                       'categoria': categoria})


def save_direccion(request):
    exito = True
    errores = []
    try:
        if request.method == 'POST':
            usuario = request.POST.get("user", None)
            user = Usuario.objects.get(id=usuario)
            dir_res = DireccionRestaurante()
            dir_res.restaurante_id = request.POST.get("rs", None)
            dir_res.ciudad_id = request.POST.get("ciudad", None)
            dir_res.ubicacion = request.POST.get("ubicacion", None)
            dir_res.latitud = request.POST.get("latitud", None)
            dir_res.longitud = request.POST.get("longitud", None)
            dir_res.estado = 1
            dir_res.full_clean()
            dir_res.save()
    except ValidationError as e:
        errores = e.messages
        exito = False

    if exito == True:
        name = user.nombreUsuario
        messages.success(request, 'La direccion se ha creado correctamente')
        response = redirect('../administrador-restaurante/'+name)
        return response

    elif exito == False:
        return JsonResponse({
            'exito': exito,
            'errores': errores
        })


def save_plato(request):
    exito = True
    errores = []
    usuario = request.POST.get("user", None)
    user = Usuario.objects.get(id=usuario)
    try:
        if request.method == 'POST':
            plato = Plato()
            plato.nombre = request.POST.get("nombre", None)
            plato.descripcion = request.POST.get("descripcion", None)
            plato.precio = request.POST.get("precio", None)
            plato.img = request.POST.get("img", None)
            plato.categoria_id = request.POST.get("cats", None)
            plato.id_restaurante_id = request.POST.get("rs", None)
            plato.full_clean()
            plato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False

    if exito == True:
        name = user.nombreUsuario
        messages.success(request, 'El plato ha sido añadido exitosamente')
        response = redirect('../administrador-restaurante/'+name)
        return response

    elif exito == False:
        return JsonResponse({
            'exito': exito,
            'errores': errores
        })