from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ActivationValidator:
    @staticmethod
    def validate(attrs):
        username = attrs.get("username")
        email = attrs.get("email")
        code = attrs.get("code")

        if not User.objects.filter(username=username, email=email, activation_code=code).exists():
            raise serializers.ValidationError("User not found")
        return attrs

    @staticmethod
    def activate(user):
        user.is_active = True
        user.activation_code = ""
        user.save()
