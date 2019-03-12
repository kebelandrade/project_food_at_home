from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.models import Usuario


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


def actualizar_usuario(req):
    pass


def eliminar_usuario(req):
    pass
