from rest_framework import status
from rest_framework.response import Response
from ..serializers.activation_serializer import ActivationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ActivationService:
    @staticmethod
    def _activate_user(email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return None
        user.activation_code = ""
        user.is_active = True
        user.save()
        return user

    @staticmethod
    def activation_post(request):
        serializer = ActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = ActivationService._activate_user(
            serializer.validated_data['email'],
            serializer.validated_data['code']
        )

        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "User activated successfully"}, status=status.HTTP_201_CREATED)