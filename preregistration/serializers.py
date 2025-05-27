from rest_framework import serializers
from .models import Preregistro

class PreregistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preregistro
        fields = ['nombre', 'email', 'ci']
