from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField( max_length=100)
    nombre_real = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_usuario