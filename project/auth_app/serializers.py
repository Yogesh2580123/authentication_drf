from django.shortcuts import render
from .models import RegisterUser
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type":"password"})
    confirm_password = serializers.CharField(write_only=True, style={"input_type":"password"})
    class Meta:
        model = RegisterUser
        fields = ["username", "email", "password", "confirm_password", "role"]
        read_only_fields = ["role"]

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        role = validated_data.pop("role", "USER").upper()
        validated_data["role"] = role
        user = RegisterUser.objects.create_user(**validated_data, password=password)
        user.save()
        return user

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("password and confirm_password do not match please check and try again")
        return data


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ["username", "password"]

    
