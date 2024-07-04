from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from authy.views import *


router = SimpleRouter()
router.register(r"register", UserRegistrationViewset, basename="signup")
urlpatterns = [
    path("users/signin", SigninView.as_view(), name="login"),
    path("users/signout", LogoutView.as_view(), name="logout"),
    path("users/verify-email", VerifyOTPView.as_view(), name="verify-otp"),
    path("users/forgot-password", ForgotPasswordView.as_view(), name="forgot-password"),
    path("users/verify-otp", ValidateOTPView.as_view()),
    path("users/request-new-otp", RequestNewOTPView.as_view(), name="request-new-otp"),
    path(
        "users/set-password/<uuid:token>",
        SetNewPasswordView.as_view(),
        name="set-new-password",
    ),
]
urlpatterns += router.urls
