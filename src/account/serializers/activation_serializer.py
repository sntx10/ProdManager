from rest_framework import serializers
from ..validators.activation_validator import ActivationValidator


class ActivationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    code = serializers.CharField()

    def validate(self, attrs):
        return ActivationValidator.validate(attrs)

    def activate(self):
        ActivationValidator.activate(self)
