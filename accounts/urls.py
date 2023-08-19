from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserRegistrationView.as_view(), name='login'),
    path('logout/', UserLoginView.as_view(), name='logout'),
]