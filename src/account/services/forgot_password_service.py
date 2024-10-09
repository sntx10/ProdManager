from ..serializers.forgot_passsword_serializer import ForgotPasswordCompleteSerializer, ForgotPasswordSerializer
from django.contrib.auth import get_user_model
from ..tasks import send_password_celery

User = get_user_model()


class ForgotPasswordService:
    @staticmethod
    def send_code(request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_password_celery(user.username, user.email, user.activation_code)
        return {"message": "Код восстановления отправлен на ваш email."}


class ForgotPasswordCompleteService:
    @staticmethod
    def complete_password(request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ""
        user.save()
        return {"message": "Пароль успешно обновлен."}

