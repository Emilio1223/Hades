from django.db import models
from datetime import datetime

# Create your models here.
class Gender(models.TextChoices):
    MALE = 'male', 'Masculino'
    FEMALE = 'female', 'Femenino'

class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Nombres')
    last_name = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=13, unique=True)
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=Gender.choices, default='male', verbose_name='Sexo')
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
  
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
