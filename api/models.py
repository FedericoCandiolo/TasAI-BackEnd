from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.Model.pk
    nombre_usuario = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    nombre_publico = models.CharField(max_length=100)
