from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import *
from django.core import serializers
from django.template.response import *
import datetime


def cliente_cat(request):
    cats = Categoria()
    cats = serializers.serialize("json", Categoria.objects.all())
    res = HttpResponse(cats, content_type="application/json")
    return res


def cliente_rest(request):
    rest = Restaurante()
    rest = serializers.serialize("json", Restaurante.objects.all())
    res = HttpResponse(rest, content_type="application/json")
    return res


def cliente_ciudad(request):
    c = Ciudad()
    c = serializers.serialize("json", Ciudad.objects.all())
    res = HttpResponse(c, content_type="application/json")
    return res


def cliente_queryciudad(request, id):
    restaurante = Restaurante()
    ciudad = Ciudad()
    direccion = DireccionRestaurante()
    # query = Restaurante()
    query = serializers.serialize("json", Restaurante.objects.filter(direccionrestaurante__ciudad = id))
    rest = HttpResponse(query, content_type='application/json')
    return rest


def cliente_restaurante_menu(request, id):
    pass


def vermenu(request, id):
    pass


def menus(request, id, idc, name):
    menu = Plato.objects.filter(id_restaurante=id)
    res = Restaurante.objects.filter(direccionrestaurante__ciudad = idc).distinct()
    restaurante = Restaurante.objects.filter(id=id)
    ciudad = Ciudad.objects.filter(id=idc)
    transporte = Transporte.objects.all()
    usuario = Usuario.objects.filter(nombreUsuario = name)
    direccion = DireccionUsuario.objects.all()
    return TemplateResponse(request, 'cliente/menu.html',{'menu': menu, 'restaurante': restaurante,
                                                          'res': res, 'ciudad': ciudad,
                                                          'transporte': transporte,
                                                          'usuario': usuario,
                                                            'direccion':direccion})

def pedido(request, id):
    query= serializers.serialize("json", Plato.objects.filter(id = id))
    plato = HttpResponse(query, content_type='application/json')
    return plato

def save_pedido(request):
    now = datetime.datetime.now()
    try:
        if request.method == 'POST':
            longitud = int(request.POST.get('longitud'))
            int(longitud)
            # pedido = Pedido()
            # pedido.fecha_pedido = now
            # pedido.calificacion = request.POST.get('calificacion', None)
            # pedido.precioPedido = request.POST.get('total', None)
            # pedido.direccion_id = request.POST.get('select_direccion', None)
            # pedido.empleado_id = request.POST.get('empleado', None)
            # pedido.transporte_id = request.POST.get('select_transporte', None)
            # pedido.usuario_id = request.POST.get('usuario', None)
            # pedido.save()

            id_pedido = Pedido.objects.all().last()
            body = BodyPedido()
            for long in range(longitud - 1):
                body.precio = request.POST.get('precio-'+str(long), None)
                body.pedido_id = id_pedido.id
                body.plato_id = request.POST.get('id_plato-'+str(long), None)
                body.save()

    except ValidationError as e:
        mensaje = e.messages
        exito = False