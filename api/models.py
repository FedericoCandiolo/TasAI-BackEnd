from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Plan(models.Model):
    id = models.Model.pk
    nombre_plan = models.CharField(max_length=20, null=True)
    precio = models.IntegerField(default=1000,
                                 validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=9999999)])
    tasaciones_maximas = models.IntegerField(default=50, validators=[MinValueValidator(limit_value=1),
                                                                     MaxValueValidator(limit_value=9999)])
    guardados_maximos = models.IntegerField(default=50, validators=[MinValueValidator(limit_value=1),
                                                                    MaxValueValidator(limit_value=9999)])
    activo = models.BooleanField(default=True)  # Vigente = 1, No Vigente = 0


class Usuario(AbstractUser):
    id = models.Model.pk
    email = models.CharField(max_length=50, null=True)
    estado = models.BooleanField(default=True)  # Activado = 1, Bloqueado = 0
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1)  # id_plan
    tasaciones_realizadas = models.IntegerField(default=0, validators=[MinValueValidator(limit_value=0),
                                                                       MaxValueValidator(limit_value=9999)])
    guardados_realizadas = models.IntegerField(default=0, validators=[MinValueValidator(limit_value=0),
                                                                      MaxValueValidator(limit_value=9999)])

    def __str__(self):
        return self.username


class Propiedad(models.Model):
    id = models.Model.pk
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    calle = models.CharField(max_length=50, null=True)
    numero = models.IntegerField(null=True,
                                 validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=9999)])
    habitaciones = models.IntegerField(default=0,
                                       validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=20)])
    baños = models.IntegerField(default=0,
                                validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=20)])
    toilets = models.IntegerField(default=0,
                                  validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=20)])
    dormitorios = models.IntegerField(default=0,
                                      validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=20)])
    pisos = models.IntegerField(default=0,
                                validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=20)])
    pileta = models.BooleanField(default=False)
    parrilla = models.BooleanField(default=False)
    jardin = models.BooleanField(default=False)
    latitud = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitud = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    esta_guardado = models.BooleanField(default=False)

    # class Meta:
    #     unique_together = ('id_usuario', 'calle', 'numero')


class Tasacion(models.Model):
    id = models.Model.pk
    id_propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, default=1)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    fecha_tasacion = models.DateTimeField(auto_now_add=True)
    precio = models.IntegerField(null=True,
                                 validators=[MinValueValidator(limit_value=1), MaxValueValidator(limit_value=9999999)])
    esta_guardado = models.BooleanField(default=False)
