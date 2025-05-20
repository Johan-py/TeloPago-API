from rest_framework import serializers
from .models import CustomUser

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('nombre', 'apellido', 'email', 'carnet', 'fecha_nacimiento', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'email', 'fecha_nacimiento', 'carnet', 'balance']
        read_only_fields = ['email']  # O quita si quieres permitir actualizar email