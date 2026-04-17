from django.shortcuts import render
# importación necesaria
from django.http import HttpResponse

# Create your views here.

# primer método de la vista
def hola_mundo(request):
    return HttpResponse("Hola Mundo!!!")

