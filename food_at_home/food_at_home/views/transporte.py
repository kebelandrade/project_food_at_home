from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import Transporte
from django.core import serializers


def crear_transporte(req):
    errores = []
    exito = True
    try:
        trans = Transporte()
        trans.nombre = req.POST.get("nombre", None)
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_transporte(req, id):
    errores = []
    exito = True
    try:
        trans = Transporte.objects.filter(id=id).first()
        trans.nombre = req.POST.get("nombre", '')
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def ver_transporte(request):
    if 'nombre' in request.GET:
        transporte = serializers.serialize("json",
                                     Transporte.objects.filter(
                                         nombre__icontains=request.GET['nombre']
                                     ))
    else:
        transporte = serializers.serialize("json", Transporte.objects.all())
    return HttpResponse(transporte, content_type='application/json')
