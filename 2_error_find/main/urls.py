from django.urls import path
from .views import (
    Test, 
    Home,
    Student_one,
    Add_,
    load_schools,
)

urlpatterns = [
    path("", Home, name="H"),
    path("test/", Test, name="T"),
    path("one/<pk>/", Student_one, name="S"),
    path("add/", Add_, name="A"),
    path("ajax/load_schools/", load_schools, name="load_maktab"),
]