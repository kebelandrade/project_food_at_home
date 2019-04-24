from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario, Restaurante, Categoria, Ciudad
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import *
from django.template import *
from django.shortcuts import redirect
from django.contrib import messages


def root(request):
    return render(request, 'administrador/root.html')


def inicio(request):
    ciudad = Ciudad.objects.all()
    return TemplateResponse(request, 'Index2.html', {'ciudad': ciudad})


def categorias(request):
    cats = serializers.serialize("json", Categoria.objects.all())
    res = HttpResponse(cats, content_type="application/json")
    return res


def allrestaurante(request):
    restaurante = serializers.serialize("json", Restaurante.objects.filter(estado='1'))
    resta = HttpResponse(restaurante, content_type="application/json")
    return resta


def ver_res(request, id):
    #return HttpResponse(id)
    restaurantes = serializers.serialize('json', Restaurante.objects.filter(categoriarestaurante__id_categoria=id))
    return HttpResponse(restaurantes, content_type='application/json')


def login(request):

    errores = []
    exito = True

    correo = request.POST.get('correo')
    password = request.POST.get('password')
    validar = request.POST.get('validar')

    if request.method == 'POST':
        usuario = Usuario.objects.get(email=correo,password=password)
        exito = True
    else:
        exito = False
#

    if exito == False:
        return render(request, 'Index2.html')
    elif exito == True:
        if usuario.tipoUsuario == 1:
            response = redirect('administrador/root.html')
            return response
        elif usuario.tipoUsuario == 2:
            name = usuario.nombreUsuario
            response = redirect('cliente/inicio_usuario_cliente.html/'+name)
            return response
        elif usuario.tipoUsuario == 3:
            name = usuario.nombreUsuario
            response = redirect('administrador-restaurante/'+name)
            return response

            
def inicio2(request):
    id = request.POST.get('selectCiudad')
    query = serializers.serialize("json",Restaurante.objects.filter(direccionrestaurante__ciudad = id))
    rest = HttpResponse(query, content_type='application/json')
    return rest


def inicio3(request, id):
    query = serializers.serialize("json",Restaurante.objects.filter(direccionrestaurante__ciudad = id))
    rest = HttpResponse(query, content_type='application/json')
    return rest


def espacio(request):
    exito = True
    error = []
    try:
        if request.method == 'POST':
            usuario = Usuario()
            restaurante = Restaurante()
            usuario.nombre = request.POST.get('nombre', None)
            usuario.apellidos = request.POST.get('apellido', None)
            usuario.nombreUsuario = request.POST.get('usuario', None)
            usuario.password = request.POST.get('contrasena', None)
            usuario.telefono = request.POST.get('telefono', None)
            usuario.email = request.POST.get('email',None)
            usuario.tipoUsuario = request.POST.get('tipoU', None)
            usuario.save()

            id_usuario = Usuario.objects.all().last()

            restaurante.nombre = request.POST.get('restaurante', None)
            restaurante.telefono = request.POST.get('tel', None)
            restaurante.estado = request.POST.get('estado', None)
            restaurante.calificacion = request.POST.get('calificacion', None)
            restaurante.img= request.FILES['img']
            restaurante.usuario_id = id_usuario.id
            restaurante.save()
            exito = True
    except error as e:
        exito = False

    if exito == True:
        messages.success(request, 'La solicitud de tu restuarente se esta procesando, te llamaremos a tu numero celular cuando se acepte la solicitud')
        return redirect('/')
    elif exito == False:
        messages.error(request, 'La solicitud de tu restuarente fallo, revisa los campos del formulario nuevamente')
        return redirect('/')
