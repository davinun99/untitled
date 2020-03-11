from django.db import models

# Create your models here. lista_permisos = ArrayField
class Usuario(models.Model):
    nombre_usuario = models.CharField( max_length=100)
    nombre_real = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    contrasegna = models.CharField(max_length=200, default="empty")

    def __init__(self, nombre_usuario="vacio", nombre_real="vacio", email="vacio", contrasegna="vacio"):
        self.nombre_usuario = nombre_usuario
        self.nombre_real = nombre_real
        self.email = email
        self.contrasegna = contrasegna

    def __str__(self):
        return self.nombre_usuario