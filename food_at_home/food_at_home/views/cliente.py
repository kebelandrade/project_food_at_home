from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from ..models import Categoria, Restaurante, Ciudad, DireccionRestaurante,Plato
from django.core import serializers
from django.template.response import *


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
    query = serializers.serialize("json",Restaurante.objects.filter(direccionrestaurante__ciudad = id))
    rest = HttpResponse(query, content_type='application/json')
    return rest


def cliente_restaurante_menu(request, id):
    pass


def vermenu(request, id):
    pass


def menus(request, id, idc):
    menu = Plato.objects.filter(id_restaurante = id)
    res = Restaurante.objects.filter(direccionrestaurante__ciudad=idc).distinct()
    restaurante = Restaurante.objects.filter(id=id)
    ciudad = Ciudad.objects.filter(id=idc)
    return TemplateResponse(request, 'cliente/menu.html',{'menu':menu, 'restaurante':restaurante, 'res':res,'ciudad':ciudad})
