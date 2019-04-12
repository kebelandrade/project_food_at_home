from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario, Categoria
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import *
from django.template import *
from ..models import Empleado
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, "administrador/root.html")


def gestion_usuarios(request):
    empleados = Empleado.objects.all()
    return TemplateResponse(request, 'administrador/Empleado.html', {'empleados': empleados})


def gestion_restaurante(request):
    return render(request, 'administrador/Restaurantes.html')


def gestion_ciudades(request):
    return render(request, 'administrador/ciudad.html')

def saveCategoria(request):
    errores = []
    exito = True
    img = []
    try:
        nueva_categoria = Categoria()
        nueva_categoria.nombre = request.POST.get('nombre', None)
        file = request.FILES['img']
        fs = FileSystemStorage(location='/media/photos')
        filename = fs.save(nueva_categoria.img, file)
        nueva_categoria.descripcion = request.POST.get('descripcion', None)
        nueva_categoria.full_clean()
        nueva_categoria.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores,
    })
