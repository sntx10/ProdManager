from django.urls import path
from .views import (
    RegisterView, ActivationViewCode,
    ChangePasswordView, ForgotPasswordView,
    ForgotPasswordCompleteView, ActivationViewDjCode,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", RegisterView.as_view()),
    path(
        "activate/<str:email>/<str:activation_code>/",
        ActivationViewDjCode.as_view(),
        name="activate",
    ),
    path("activate_code/", ActivationViewCode.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("lose_password/", ForgotPasswordView.as_view()),
    path("lose_confirm_code/", ForgotPasswordCompleteView.as_view(), name="forgot"),
]