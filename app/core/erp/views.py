from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from core.erp.models import Category, Product
# Create your views here.

# def myfirstview(request):
#     return HttpResponse('Hola Mundo') 

# def myfirstview(request):
#     data = {
#         'name': 'Hades',
#         'lastname': 'Django',
#         'age': 1,
#     }
#     return JsonResponse(data)
def myfirstview(request):
    data = {
        'name': 'Emilio',
        'lastname': 'Rodriguez',
        'age': 1,
        'categorias' : Category.objects.all(),
    }
    return render(request, 'home.html', data)

def secondview(request):
    data = {
        'name': 'Javier',
        'productos' : Product.objects.all(),}
    return render(request, 'second.html', data)