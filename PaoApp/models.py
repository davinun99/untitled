from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario( models.Model ):
    nombre_usuario = models.CharField( max_length=200 )
    email = models.CharField(max_length=200)
