from django.shortcuts import render


def login(request):
    return render(request, 'login/login.html')

def usuario_nuevo(request):
    return render(request, 'login/Usuario_Nuevo.html')