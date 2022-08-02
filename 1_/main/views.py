from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def Test(request):
    return HttpResponse("Hello World :)")

def All_Students(request):
    stu = Student.objects.all()
    gra_9 = Student.objects.all()
    return render(request, "index.html", context={"student":stu, "gra_9":gra_9})