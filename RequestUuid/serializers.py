from rest_framework import serializers
from .models import UUIDGenerator


class UUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUIDGenerator
        fields = '__all__'
