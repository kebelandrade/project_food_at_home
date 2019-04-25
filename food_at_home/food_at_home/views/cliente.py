from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import *
from django.core import serializers
from django.template.response import *
import datetime
from django.shortcuts import redirect



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
    exito = True
    usuario = int(request.POST.get('usuario', None))
    id = usuario
    try:
        pass
        if request.method == 'POST':
            longitud = int(request.POST.get('longitud'))
            int(longitud)
            pedido = Pedido()
            pedido.fecha_pedido = now
            pedido.calificacion = request.POST.get('calificacion', None)
            pedido.precioPedido = request.POST.get('total', None)
            pedido.direccion_id = request.POST.get('select_direccion', None)
            pedido.empleado_id = request.POST.get('empleado', None)
            pedido.transporte_id = request.POST.get('select_transporte', None)
            pedido.usuario_id = request.POST.get('usuario', None)
            pedido.estado = "0"
            pedido.save()

            id_pedido = Pedido.objects.all().last()

            for long in range(longitud):
                body = BodyPedido()
                body.precio = request.POST.get('precio-'+str(long), None)
                body.pedido_id = id_pedido.id
                body.plato_id = request.POST.get('id_plato-'+str(long), None)
                body.save()
            exito = True
    except ValidationError as e:
        exito = False

    if exito == True:

        response = redirect('/cliente/'+str(id)+'/pedidos')
        return response
    elif exito == False:
        pass


def verResta(request, id):
    usuario = Usuario.objects.filter(id=id)
    pedidos = Pedido.objects.filter(usuario_id = id)
    body = BodyPedido.objects.all()
    restaurante = Restaurante.objects.all()
    plato = Plato.objects.filter()

    return TemplateResponse(request,'cliente/pedidos.html',{'usuario':usuario,
                                                            'pedido': pedidos,
                                                            'restaurante': restaurante,
                                                            'platos': plato,
                                                            'body': body})
