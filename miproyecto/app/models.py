from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
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
    birth_date(
        help_text="Fecha de nacimiento"
    )
    role = models.CharField(
        max_length=10,
        choices=[
            ('admin', 'Administrador'), ('editor', 'Editor'),
            ('cliente', 'Cliente')
        ],
        default='cliente',
        help_text="Rol del usuario."
    )
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.role})"
    