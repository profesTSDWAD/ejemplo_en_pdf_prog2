from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Role(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="nombre del rol."
    )
    description = models.TextField(
        blank=True,
        help_text="Descripción del rol."
    )
    def __str__(self) -> str:
        return self.name

class Users(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Nombre completo del usuario."
    )
    email = models.EmailField(
        unique=True,
        help_text="Correo electrónico único."
    )
    dni = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(r'\d{7,8}$')],
        help_text="Número de documento (7 u 8 dígitos)."
    )
    birth_date = models.DateField(
        help_text="Fecha de nacimiento"
    )
    # originalmente era un CharField ahora es ForeignKey
    role = models.ForeignKey(Role, on_delete=models.CASCADE,
                             related_name='users')

    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.role})"

