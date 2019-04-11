from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario, Categoria
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import *
from django.template import *
from ..models import Empleado


def index(request):
    return render(request, "administrador/root.html")


def gestionUsuarios(request):
    empleados = Empleado.objects.all()
    return TemplateResponse(request, 'administrador/Empleado.html',{'empleados':empleados})

def gestionRestaurante(request):
    return render(request, 'administrador/Restaurantes.html')

def gestionCiudades(request):
    return render(request, 'administrador/ciudad.html')

def saveCategoria(request):
    # errores = []
    # exito = True
    # try:
    #     nueva_categoria = Categoria()
    #     nuevo_categoria.nombre = req.POST.get('nombre', None)
    #     nuevo_usuario.apellidos = req.POST.get('apellido', None)
    #     nuevo_usuario.full_clean()
    #     nuevo_usuario.save()
    # except ValidationError as e:
    #     errores = e.messages
    #     exito = False
    # return JsonResponse({
    #     'exito': exito,
    #     'errores': errores
    # })
    return "hola"
