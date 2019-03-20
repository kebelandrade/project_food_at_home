from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import Usuario
from django.core import serializers


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


def ver_usuario(request):
    if 'nombre' in request.GET:
        usuario = serializers.serialize("json",
                                     Usuario.objects.filter(
                                         nombre__icontains=request.GET['nombre']
                                     ))
    else:
        usuario = serializers.serialize("json", Usuario.objects.all())
    return HttpResponse(usuario, content_type='application/json')


def eliminar_usuario(req):
    pass
