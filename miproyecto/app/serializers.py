# serializers.py debe ser creado explicitamente,
# el framework no lo créa por defecto
from rest_framework import serializers
from .models import User, Role

class RoleSerializer(serializers.ModelSerializer):
    # serializer anidado desde el lado "uno"
    # debe usarse en uno u otro lado, en ambos genera ref. circular
    #users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'description']
class UserSerializer(serializers.ModelSerializer):
    # serializer anidado desde el lado "muchos"
    role = RoleSerializer(read_only=True)
    
    class Meta:
        model= User
        # esto incluye todos los campos
        #fields= '__all__'
        fields= ['id', 'name', 'email', 'dni', 'birth_date', 'role',
                 'activo']
