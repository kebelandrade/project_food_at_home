from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import Categoria
from django.core import serializers


def crear_categoria(request):
    errores = []
    exito = True
    try:
        nuevo_empleado = Categoria()
        nuevo_empleado.nombre = request.POST.get('nombre', None)
        nuevo_empleado.full_clean()
        nuevo_empleado.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def ver_categoria(request):
    if 'nombre' in request.GET:
        categoria = serializers.serialize("json", Categoria.objects.filter(nombre__icontains=request.GET['nombre']))
    else:
        categoria = serializers.serialize("json", Categoria.objects.all())
    return HttpResponse(categoria, content_type="application/json")


def actualizar_categoria(request, id):
    errores = []
    exito = True
    try:
        actualizar_categoria = Categoria.objects.filter(id=id).first()
        actualizar_categoria.nombre = request.POST.get['nombre', '']
        actualizar_categoria.full_clean()
        actualizar_categoria.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'Exito': exito,
        'Errores': errores
    })
