from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_legth=40)
    camada = models.IntegerField()