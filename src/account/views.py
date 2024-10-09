from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.login_serializer import LoginSerializer
from .serializers.forgot_passsword_serializer import ForgotPasswordSerializer, ForgotPasswordCompleteSerializer

from .services.registration_service import RegistrationService
from .services.activation_service import ActivationService
from .services.change_password_service import ChangePasswordService
from .services.forgot_password_service import ForgotPasswordService, ForgotPasswordCompleteService

User = get_user_model()


class RegisterView(APIView):
    service = RegistrationService()

    def post(self, request):
        status_code = self.service.register(request.data)
        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)


class ActivationViewCode(APIView):
    service = ActivationService()

    def post(self, request):
        status_code = self.service.activation_post(request)
        return Response("Активация прошла успешно", status=status_code)


class ActivationViewDjCode(View):
    template_name = "activate.html"
    service = ActivationService()

    def get(self, request, email, activation_code):
        self.service._activate_user(email, activation_code)
        return render(request, self.template_name)


class LoginViewEmail(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            ChangePasswordService.change_password(request)
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(generics.CreateAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = ForgotPasswordService.send_code(request)
        return Response(response, status=status.HTTP_200_OK)


class ForgotPasswordCompleteView(generics.CreateAPIView):
    serializer_class = ForgotPasswordCompleteSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = ForgotPasswordCompleteService.complete_password(request)
        return Response(response, status=status.HTTP_200_OK)


