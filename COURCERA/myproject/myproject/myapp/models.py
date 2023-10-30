from django.db import models

# Create your models here.

class Bebidas(models.Model):
    nombre_bebida = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la categoría")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey("CategoriaDeBebidas", on_delete=models.SET_NULL, null=True, blank=True)
    #relación de uno a muchos entre CategoriaDeBebidas y Bebidas

class CategoriaDeBebidas(models.Model):
    nombre = models.CharField(max_length=100, unique=True, help_text="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la categoría")
    #bebida = models.ForeignKey('Bebidas', on_delete=models.SET_NULL, null=True, blank=True)

class Booking(models.Model):
    fecha = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    reservation_time = models.DateTimeField(auto_now=True)
    guest_count = models.IntegerField
    comments = models.CharField(max_length=1000)

    # Otros campos de reserva
    


