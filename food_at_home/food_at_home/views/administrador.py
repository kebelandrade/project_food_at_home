from django.shortcuts import render
from django.shortcuts import render_to_response
from ..models import Usuario
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core import serializers
from django.template.response import *
from django.template import *

def index(request):
    return render(request, "administrador/root.html")
