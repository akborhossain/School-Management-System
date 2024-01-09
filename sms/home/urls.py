from django.urls import path
from .views import CreateUser ,ForgotPassword

urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup'),
    path('forgot_password/',ForgotPassword.as_view(), name='forgotpassword'),
]