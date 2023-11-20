from django.contrib import admin
from .models import Bebidas
from .models import CategoriaDeBebidas
from .models import Booking
from .models import empleados

# Register your models here.

admin.site.register(Bebidas)
admin.site.register(CategoriaDeBebidas)
admin.site.register(Booking)
admin.site.register(empleados)
