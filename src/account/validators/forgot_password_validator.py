from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ForgotPasswordValidator:
    @staticmethod
    def validate(email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Пользователь с таким email не существует")


class ForgotPasswordCompleteValidator:
    @staticmethod
    def validate(email, code):
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError("Пользователь не найден или код неверен")
