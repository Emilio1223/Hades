from django.db import models
from datetime import datetime
from django.forms import model_to_dict

# Create your models here.
class Gender(models.TextChoices):
    MALE = 'M', 'Masculino'
    FEMALE = 'F', 'Femenino'
    OTHER = 'O', 'Otro'

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dict(self)
        model_to_dict 
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering = ['id']
        
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

class Sale (models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Creacion')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Sale {self.id} - {self.client.first_name} {self.client.last_name}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
        
class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
        ordering = ['id']
        
