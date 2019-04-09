from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import TemplateResponse

def inicio(request):
    return render(request, 'Index.html')

def login(request):
    return render(request, 'login/login.html')

def verificar(req):
    errores = []
    exito = True
    pagina = 'login/login.html'
    correo = req.POST.get('correo')
    password = req.POST.get('contra')

    try:
        usuario = Usuario.objects.filter(['email','password'])
        

        # correo2 = usuario['email']
        # if usuario.email == correo and usuario.password == password:
        #     if tipo_usuario == 1:
        #         exito = True
        #         pagina = 'administrador/empleado.html'
    except Exception as e:
        errores = e.messages
        exito = False
        pagina = 'login/login.html'

    if exito == True:
        return JsonResponse({
            'exito': exito,
            'errores': errores,
            'pagina': pagina,
            'correo': correo,
            'password': password,
            # 'correo2': us
            # 'password2': usuario.password
            })
    elif exito == False:
        return JsonResponse({
            'exito': exito,
            'errores': errores,
            'pagina': pagina
            })
