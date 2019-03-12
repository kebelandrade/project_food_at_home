from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import Restaurante, DireccionRestaurante
from django.core import serializers


def crear_restaurante(request):
    errores = []
    exito = True
    try:
        nuevo_restaurante = Restaurante()
        nuevo_restaurante.nombre = request.POST.get('nombre', None)
        nuevo_restaurante.telefono = request.POST.get('telefono', None)
        nuevo_restaurante.estado = request.POST.get('estado', None)
        nuevo_restaurante.calificacion = request.POST.get('calificacion', None)
        nuevo_restaurante.usuario = request.POST.get('usuario')
        nuevo_restaurante.full_clean()
        nuevo_restaurante.save()
    except ValidationError as e:
        errores= e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def ver_restaurante(request):
    if 'nombre' in request.GET:
        restaurante = serializers.serialize("json", Restaurante.objects.filter(nombre__icontains=request.GET['nombre']))
    else:
        restaurante = serializers.serialize("json", Restaurante.objects.all())
    return HttpResponse(restaurante, content_type="application/json")


def actualizar_restaurante(request, id):
    errores = []
    exito = True
    try:
        res = Restaurante.objects.filter(id=id).first()
        res.nombre = request.POST.get['nombre','']
        res.telefono = request.POST.get['telefono','']
        res.full_clean()
        res.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'Exito': exito,
        'Errores': errores
    })


def crear_direccion(request):
    errores = []
    exito = True
    try:
        nueva_direccion = DireccionRestaurante()
        nueva_direccion.id = request.POST.get('id_restaurante', None)
        nueva_direccion.ciudad = request.POST.get('id_ciudad', None)
        nueva_direccion.ubicacion = request.POST.get('ubicacion', None)
        nueva_direccion.latitud = request.POST.get('latitud', None)
        nueva_direccion.longitud = request.POST.get('longitud')
        nueva_direccion.estado = request.POST.get(True, None)
        nueva_direccion.full_clean()
        nueva_direccion.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def ver_direcciones(request):
    if 'id' in request.GET:
        direccion = serializers.serialize("json", DireccionRestaurante.objects.filter(nombre__icontains=request.GET['id']))
    else:
        direccion = serializers.serialize("json", DireccionRestaurante.objects.all())
    return HttpResponse(direccion, content_type="application/json")


def actualizar_direcciones(request, id):
    errores = []
    exito = True
    try:
        direccion = DireccionRestaurante.objects.filter(restaurante=id).first()
        direccion.estador = request.POST.get['estado','']
        direccion.full_clean()
        direccion.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'Exito': exito,
        'Errores': errores
    })
