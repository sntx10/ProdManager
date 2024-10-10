from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ChangePasswordValidator:
    @staticmethod
    def validate_old_password(request, old_password):
        user = request.user
        if not user.check_password(old_password):
            raise serializers.ValidationError("Incorrect old password")
        return old_password

    @staticmethod
    def validate(attrs):
        old_password = attrs.get("old_password")
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")

        if new_password != new_password_confirm:
            raise serializers.ValidationError("Passwords do not match")
        if new_password == old_password:
            raise serializers.ValidationError("New password cannot be the same as old password")
        return attrs

    @staticmethod
    def set_new_password(user, new_password):
        user.set_password(new_password)
        user.save()
