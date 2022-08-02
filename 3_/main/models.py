from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.


class Davlat(models.Model):
    name = models.CharField(max_length=250)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tuman(models.Model):
    name = models.CharField(max_length=250)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class People(models.Model):
    f_name = models.CharField(max_length=250)
    davlat = models.ForeignKey(Davlat, on_delete=models.SET_NULL, null=True, blank=True)
    tuman = models.ForeignKey(Tuman, on_delete=models.SET_NULL, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name