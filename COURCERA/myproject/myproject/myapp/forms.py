from django import forms  # Importa el paquete Django de formularios
from .models import Booking # Importa Booking del archivo .models

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking # Especifica el modelo relacionado
        fields = '__all__'

    
