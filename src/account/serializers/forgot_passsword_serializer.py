from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..validators.forgot_password_validator import ForgotPasswordCompleteValidator, ForgotPasswordValidator
User = get_user_model()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        ForgotPasswordValidator.validate(value)
        return value


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True)

    def validate(self, attrs):
        ForgotPasswordCompleteValidator.validate(attrs['email'], attrs['code'])
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return attrs

    def set_new_password(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ""
        user.save()
