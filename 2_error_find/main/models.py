from django.db import models

# Create your models here.

status = (
    ("shaxar", "shaxar"),
    ("tuman", "tuman"),
)

class Abilty(models.Model):
    name = models.CharField(max_length=250)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tuman(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=status)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.status}'

class School(models.Model):
    name = models.CharField(max_length=250)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    f_name = models.CharField(max_length=250)
    tuman = models.ForeignKey(Tuman, on_delete=models.SET_NULL, null=True, blank=True)
    maktab = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    abilty = models.ManyToManyField(Abilty, related_name="abilty")
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.f_name
    
