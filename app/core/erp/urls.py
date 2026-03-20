
from django.urls import path

from core.erp.views import myfirstview, secondview

app_name = 'erp'

urlpatterns = [
    path('uno/', myfirstview, name='vista1'),
    path('dos/', secondview, name='vista2'),
]

