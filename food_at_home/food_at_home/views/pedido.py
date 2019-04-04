from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from food_at_home.food_at_home.models import Pedido
from django.core import serializers


def crear_pedido(req):
    errores = []
    exito = True
    try:
        pedidos = Pedido()
        pedidos.calificacion = req.POST.get("calificacion", None)
        pedidos.precioPedido = req.POST.get("precioPedido", None)
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def ver_pedido(request):
    if 'nombre' in request.GET:
        pedido = serializers.serialize("json",
                                     Pedido.objects.filter(
                                         nombre__icontains=request.GET['nombre']
                                     ))
    else:
        pedido = serializers.serialize("json", Pedido.objects.all())
    return HttpResponse(pedido, content_type='application/json')


def actualizar_pedido(req):
    errores = []
    exito = True
    try:
        pedido = Pedido.objects.filter(id=id).first()
        pedido.nombre = req.POST.get("nombre", '')
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })
