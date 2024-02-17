from django.urls import path
from .views import RegisterView, SignInView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='signin'),
]