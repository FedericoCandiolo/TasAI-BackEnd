from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import Usuario
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def hello_page(request):
    return render(request, 'hello.html')


def home_page(request):
    return render(request, 'home.html')

