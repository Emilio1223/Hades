from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

# def myfirstview(request):
#     return HttpResponse('Hola Mundo') 

def myfirstview(request):
    data = {
        'name': 'Hades',
        'lastname': 'Django',
        'age': 1,
    }
    return JsonResponse(data)