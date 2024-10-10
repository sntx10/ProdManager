from rest_framework import serializers
from ..validators.login_validator import LoginValidator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        return LoginValidator.validate(attrs)
