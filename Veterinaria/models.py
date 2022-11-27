from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=50)
