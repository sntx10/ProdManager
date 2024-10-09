from rest_framework import status
from rest_framework.response import Response
from ..serializers.change_password_serializer import ChangePasswordSerializer


class ChangePasswordService:
    @staticmethod
    def change_password(request):
        serializer = ChangePasswordSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response("Пароль успешно обновлен", status=status.HTTP_200_OK)