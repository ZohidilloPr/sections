import datetime
from django.db import models

# Create your models here.

# sinf = (
#     ("1-sinf", 1),
#     ("2-sinf", 2),
#     ("3-sinf", 3),
#     ("4-sinf", 4), 
#     ("5-sinf", 5),
#     ("6-sinf", 6),
#     ("7-sinf", 7),
#     ("8-sinf", 8),
#     ("9-sinf", 9),
#     ("10-sinf", 10),
#     ("11-sinf", 11),
# )

class School(models.Model):
    name = models.CharField(max_length=4)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Students_9(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(self.update_sinf()==11)

    # def update_sinf(self):
    #     this_year = datetime.datetime.now().year
    #     if super().enter_date.year < this_year:
    #         new_sinf = [1 for i in range((this_year - super().self.enter_date.year) - 1 )]
    #         return sum(new_sinf)    
    #     else:
    #         return self.sinf

class Student(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    sinf = models.IntegerField()
    add_time = models.DateTimeField(verbose_name="sana")    
    enter_date = models.DateField(verbose_name="Maktabga kirgan sana")

    objects = models.Manager()
    # graduet_objects_9 = Students_9()

    def __str__(self):
        return self.name

    @property
    def update_sinf(self):
        this_year = datetime.datetime.now().year
        if self.enter_date.year < this_year:
            self.sinf = [1 for i in range((this_year - self.enter_date.year) - 1 )]
            return sum(self.sinf)    
        else:
            return self.sinf
    
    @classmethod
    def graduet_9(cls):
        gra_9 = []
        for i in cls.objects.all():
            if i.update_sinf == 8:
                gra_9.append(i)
                return gra_9
        # print(gra_9)
        # gra_9 = [i for i in cls.objects.all if i.update_sinf == 8]
        # return gra_9




