from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model
from ..tasks import send_activation_code_celery

User = get_user_model()


class RegisterValidator:
    @staticmethod
    def validate(attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        if password != password_confirm:
            raise ValidationError("Password does not match")
        return attrs

    @staticmethod
    def create(validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code_celery(user.username, user.email, user.activation_code)
        return user
