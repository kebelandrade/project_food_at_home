from ..models import *
from django.core import serializers
from django.template.response import *

def inicio_admin_res(request, name):
    usuario = Usuario.objects.filter(nombreUsuario = name)
    id_usuario = Usuario.objects.get(nombreUsuario = name)
    restaurante = Restaurante.objects.filter(usuario_id = id_usuario.id)
    ciudad = Ciudad.objects.all()
    return TemplateResponse(request, 'adminRes/index_admin_res.html', {'usuario': usuario,
                                                                       'res':restaurante,
                                                                       'ciudad': ciudad})

def save_direccion(request):
    pass