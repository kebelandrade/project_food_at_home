from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import Empleado
from django.core import serializers
from django.shortcuts import render

def gestion_empleado(request):
    return render(request, 'administrador/Empleado.html')


def crear_empleado(request):
    errores = []
    exito = True
    try:
        nuevo_empleado = Empleado()
        nuevo_empleado.identidad = request.POST.get('identadad', None)
        nuevo_empleado.nombre_completo = request.POST.get('nombre_completo', None)
        nuevo_empleado.usuario = request.POST.get('usuario', None)
        nuevo_empleado.password = request.POST.get('password', None)
        nuevo_empleado.telefono = request.POST.get('telefono', None)
        nuevo_empleado.estado = request.POST.get('estado', None)
        nuevo_empleado.full_clean()
        nuevo_empleado.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_empleado(request, id):
    if 'nombre' in request.GET:
        empleado = serializers.serialize("json", Empleado.objects.filter(nombre__icontains=request.GET['nombre']))
    else:
        empleado = serializers.serialize("json", Empleado.objects.all())
    return HttpResponse(empleado, content_type="application/json")


def actualizar_empleados(request, id):
    errores = []
    exito = True
    try:
        actualizar_empleado = Empleado.objects.filter(id=id).first()
        actualizar_empleado.identidad = request.POST.get['identidad', '']
        actualizar_empleado.nombre_completo = request.POST.get['nombre', '']
        actualizar_empleado.password = request.POST.get['password', '']
        actualizar_empleado.telfono = request.POST.get['telefono', '']
        actualizar_empleado.full_clean()
        actualizar_empleado.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'Exito': exito,
        'Errores': errores
    })
