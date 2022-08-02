from django.urls import path
from .views import Test, All_Students

urlpatterns = [
    path("test/", Test, name="T"),
    path("", All_Students, name="S"),
]