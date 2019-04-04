from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')
