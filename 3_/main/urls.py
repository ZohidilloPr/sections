from django.urls import path
from .views import (Home, Add_, load_tuman)

urlpatterns = [
    path("", Home, name="HM"),
    path("add/", Add_, name="A"),
    path("load_tuman/", load_tuman, name="load_tuman"),
]