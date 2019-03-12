from django.http import HttpResponse, JsonResponse


def inicio(request):
    return HttpResponse("Food At Home")
