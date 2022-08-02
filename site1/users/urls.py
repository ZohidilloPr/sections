from django.urls import path
from .views import (
    Home,
    SignUp, 
    Login, 
    Logout,
)
 
app_name = 'users'

urlpatterns = [
    path("", Home, name="HM"),
    path("signup/", SignUp, name="SI"),
    path("login/", Login, name="LI"),
    path("logout/", Logout, name="LO"),
]
