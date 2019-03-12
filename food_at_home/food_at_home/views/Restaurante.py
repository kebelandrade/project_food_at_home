from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import Restaurante
from django.core import serializers


def crear_restaurante(request):
    errores = []
    exito = True
    try:
        nuevo_restaurante = Restaurante()
        nuevo_restaurante.nombre = request.POST.get('nombre', None)
        nuevo_restaurante.telefono = request.POST.get('telefono', None)
        nuevo_restaurante.estado = request.POST.get(True, None)
        nuevo_restaurante.calificacion = request.POST.get(0, None)
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

