# serializers.py debe ser creado explicitamente,
# el framework no lo créa por defecto
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        # esto incluye todos los campos
        fields= '__all__'
