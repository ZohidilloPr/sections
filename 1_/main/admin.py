from django.contrib import admin
from .models import School, Student


# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_time')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'enter_date')