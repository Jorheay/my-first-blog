from django.shortcuts import render
from .models import genNum
import os
ruta = os.getcwd()
ruta = ruta.replace(os.sep, "/")

# Create your views here.

def post_pruebas(request):
    posts = genNum.objects.all()
    return render(request, f'{ruta}/blog/templates/blog/prueba2.html', context={'posts': posts})