from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class LoginValidator:
    @staticmethod
    def validate(attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise ValidationError("Username and password are required")

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Invalid username or password")

        attrs["user"] = user
        return attrs
