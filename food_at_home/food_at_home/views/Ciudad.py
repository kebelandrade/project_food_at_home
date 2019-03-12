from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import Ciudad
from django.core import serializers

def crear_ciudad(request):
    errores = []
    exito = True
    try:
        nueva_ciudad = Ciudad()
        nueva_ciudad.nombre = request.POST.get('nombre', None)
        nueva_ciudad.full_clean()
        nueva_ciudad.save()
    except ValidationError as e:
        errores= e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })
def ver_ciudad(request):
    if 'nombre' in request.GET:
        ciudad = serializers.serialize("json", Ciudad.objects.filter(nombre__icontains=request.GET['nombre']))
    else:
        ciudad = serializers.serialize("json", Ciudad.objects.all())
    return HttpResponse(ciudad, content_type="application/json")

def actualizar_ciudad(request, id):
    errores = []
    exito = True
    try:
        res = Ciudad.objects.filter(id=id).first()
        res.nombre = request.POST.get['nombre', '']
        res.full_clean()
        res.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'Exito': exito,
        'Errores': errores
    })