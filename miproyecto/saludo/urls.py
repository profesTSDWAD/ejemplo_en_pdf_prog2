from django.urls import path

# importación de las vistas
from .views import hola_mundo

# configuración de las rutas del módulo
urlpatterns = [
    path('', hola_mundo),
]
