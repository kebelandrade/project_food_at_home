from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import *
from django.template import *
from django.shortcuts import redirect

def root(request):
    return render(request, 'administrador/root.html')

def inicio(request):

    return render(request, 'Index.html')

def recintes(request):
    pass

def login(request):

    errores = []
    exito = True

    correo = request.POST.get('correo')
    password = request.POST.get('contra')
    validar = request.POST.get('validar')

    if validar == 'si':
        usuario = Usuario.objects.all().filter(email="correo",password="password")
        exito = True
    else:
        exito = False

    if exito == False:
        return render(request, 'login/login.html')
    elif exito == True:
        response = redirect('administrador/index')
        return response

   # def verificar(req):
#     errores = []
#     exito = True
#     correo = req.POST.get('correo')
#     password = req.POST.get('contra')
#
#
#     try:
#         usuario = Usuario.objects.filter(['email','password'])
#
#
#         # correo2 = usuario['email']
#         # if usuario.email == correo and usuario.password == password:
#         #     if tipo_usuario == 1:
#         #         exito = True
#         #         pagina = 'administrador/empleado.html'
#     except Exception as e:
#         errores = e.messages
#         exito = False
#         pagina = 'login/login.html'
#
#     if exito == True:
#         return render(req,'login/login.html')
#
#     elif exito == False:
#         return JsonResponse({
#             'exito': exito,
#             'errores': errores,
#             'pagina': pagina
#             })
