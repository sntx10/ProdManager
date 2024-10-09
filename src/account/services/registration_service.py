from rest_framework import status
from ..serializers.register_serializer import RegisterSerializer


class RegistrationService:
    @staticmethod
    def register(data):
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return status.HTTP_201_CREATED
