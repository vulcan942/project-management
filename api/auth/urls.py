from django.urls import path
from .views import UserRegistrationView, LoginView

urlpatterns = [
    path('auth/register',UserRegistrationView.as_view()),
    path('auth/login',LoginView.as_view())
]
