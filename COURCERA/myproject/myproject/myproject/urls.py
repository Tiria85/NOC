"""
Configuración de URL para el proyecto myproject.

La lista `urlpatterns` dirige las URL a las vistas. Para obtener más información, consulte:
     https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vistas de funciones
     1. Agregue una importación: desde las vistas de importación de my_app
     2. Agregue una URL a urlpatterns: ruta('', views.home, nombre='home')
Vistas basadas en clases
     1. Agregue una importación: desde other_app.views import Inicio
     2. Agregue una URL a urlpatterns: ruta('', Home.as_view(), nombre='home')
Incluyendo otra URLconf
     1. Importe la función include(): desde django.urls importe include, ruta
     2. Agregue una URL a urlpatterns: ruta('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *  # Importa todas las funciones y variables
import myapp.views as myapp  # Dale un alias al módulo completo

from Little_Lemon.views import *
import Little_Lemon.views as little

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('home/', myapp.home),
    path('', little.index),
    path('index', myapp.index),
    
=======
    path('home/', views.home),
    path('', views.index),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
>>>>>>> a11a45d4c3cb08c0b881c325fe777e6b045d6397
]
