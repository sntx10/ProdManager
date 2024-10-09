from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..validators.register_validator import RegisterValidator

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, attrs):
        return RegisterValidator.validate(attrs)

    def create(self, validated_data):
        return RegisterValidator.create(validated_data)
