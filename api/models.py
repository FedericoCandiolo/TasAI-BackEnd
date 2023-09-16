from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Plan(models.Model):
    id_plan = models.IntegerField(primary_key=True, default=0)
    nombre_plan = models.CharField(max_length=20, null=True)
    precio = models.IntegerField(default=1000)
    tasaciones_maximas = models.IntegerField(default=50)
    guardados_maximos = models.IntegerField(default=50)
    activo = models.BooleanField(default=True)  # Vigente = 1, No Vigente = 0


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, default=0)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    apodo = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)
    estado = models.BooleanField(default=True)  # Activado = 1, Bloqueado = 0
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=0)  # id_plan
    tasaciones_realizadas = models.IntegerField(default=0)
    guardados_realizadas = models.IntegerField(default=0)


class Propiedad(models.Model):
    id_propiedad = models.IntegerField(primary_key=True, default=0)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)
    calle = models.CharField(max_length=50, null=True)
    numero = models.IntegerField(null=True)
    habitaciones = models.IntegerField(default=0)
    baños = models.IntegerField(default=0)
    toilets = models.IntegerField(default=0)
    dormitorios = models.IntegerField(default=0)
    pisos = models.IntegerField(default=0)
    pileta = models.BooleanField(default=False)
    parrilla = models.BooleanField(default=False)
    jardin = models.BooleanField(default=False)
    latitud = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitud = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)


class Tasacion(models.Model):
    id_tasacion = models.IntegerField(primary_key=True, default=0)
    id_Propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, default=0)
    fecha_tasacion = models.DateTimeField(default=datetime.now())
    precio = models.IntegerField(null=True)
    moneda = models.CharField(max_length=3, null=True)