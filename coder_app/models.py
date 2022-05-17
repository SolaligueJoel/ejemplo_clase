from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.BigIntegerField()
    fecha_nacimiento=models.DateField()
    altura=models.FloatField()
    color_de_ojos=models.CharField(max_length=30) 
    ocupacion=models.CharField(max_length=30)