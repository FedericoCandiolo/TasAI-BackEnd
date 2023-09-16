from rest_framework import viewsets
from .serializer import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer


class TasacionViewSet(viewsets.ModelViewSet):
    queryset = Tasacion.objects.all()
    serializer_class = TasacionSerializer


def hello_page(request):
    return render(request, 'hello.html')


def home_page(request):
    return render(request, 'home.html')
