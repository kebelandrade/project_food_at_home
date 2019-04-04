from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import Plato
from django.core import serializers


def crear_plato(request):
    errores = []
    exito = True
    try:
        nuevo_plato = Plato()
        nuevo_plato.nombre = request.POST.get('nombre', None)
        nuevo_plato.descripcion = request.POST.get('descripcion', None)
        nuevo_plato.categoria = request.POST.get('id_categoria', None)
        nuevo_plato.precio = request.POST.get('precio', None)
        nuevo_plato.img = request.POST.get('img', None)
        nuevo_plato.full_clean()
        nuevo_plato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def ver_plato(request, id):
    plato = Plato.objects.filter(categoria=id).first()
    return JsonResponse({
        'nombre': plato.nombre,
        'descripcion': plato.descripcion,
        'id_categoria': plato.categoria,
        'precio': plato.precio,
        'img': plato.img
    })


def actualizar_plato(request, id):
    errores = []
    exito = True
    try:
        actualizar_plato = Plato.objects.filter(categoria=id).first()
        actualizar_plato.nombre = request.POST.get['nombre', '']
        actualizar_plato.descripcion = request.POST.get['descripcion', '']
        actualizar_plato.precio = request.POST.get['precio', '']
        actualizar_plato.categoria = request.POST.get['categoria', '']
        actualizar_plato.img = request.POST.get['img', '']
        actualizar_plato.full_clean()
        actualizar_plato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'Exito': exito,
        'Errores': errores
    })
