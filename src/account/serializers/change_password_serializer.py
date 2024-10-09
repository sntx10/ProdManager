from rest_framework import serializers
from ..validators.change_password_validator import ChangePasswordValidator


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=6, required=True)
    new_password = serializers.CharField(min_length=6, required=True)
    new_password_confirm = serializers.CharField(min_length=6, required=True)

    def validate(self, attrs):
        return ChangePasswordValidator.validate(attrs, self.context)

    def save(self):
        ChangePasswordValidator.set_new_password(self)

