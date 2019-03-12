from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import DireccionUsuario
from django.core import serializers


def crear_dir_usuario(req):
    errores = []
    exito = True
    try:
        nueva_dir_usuario = DireccionUsuario()
        nueva_dir_usuario.nombre = req.POST.get("nombre", None)
        nueva_dir_usuario.direccion = req.POST.get("direccion", None)
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_dir_usuario(req, id):
    errores = []
    exito = True
    try:
        direc = DireccionUsuario.objects.filter(id=id).first()
        direc.nombre = req.POST.get("nombre", '')
        direc.direccion = req.POST.get("direccion", '')
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def eliminar_dir_usuario(req):
    pass


def ver_dir_usuario(request):
    if 'nombre' in request.GET:
        direcciones = serializers.serialize("json",
                                     DireccionUsuario.objects.filter(
                                         nombre__icontains=request.GET['nombre']
                                     ))
    else:
        direcciones = serializers.serialize("json", DireccionUsuario.objects.all())
    return HttpResponse(direcciones, content_type='application/json')
