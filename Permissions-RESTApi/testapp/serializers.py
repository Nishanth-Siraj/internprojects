from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import CustomUser

class UserTestSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'role']

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return CustomUser.objects.create(**validated_data)