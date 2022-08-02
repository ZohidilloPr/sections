from django.shortcuts import render, HttpResponse, redirect
from .models import School, Student, Tuman
from .forms import AddStudent
from django.views.generic.edit import CreateView
# Create your views here.
def Test(request):
    return HttpResponse("Hello World :)")

def Home(request):
    stu = Student.objects.all()
    return render(request, "home.html", context={
        "stu":stu,
    })

def Student_one(request, pk):
    one = Student.objects.get(pk=pk)
    return render(request, "one.html", context={
        "one": one,
        "pk":pk,
    })                                                                  

def Add_(request):
    if request.method == "POST":
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect("H")
    form = AddStudent
    return render(request, 'add.html', context={
        "form":form
    })

def load_schools(request):
    tuman_id = request.GET.get("tuman_id")
    maktab = School.objects.filter(tuman_id=tuman_id).all()
    return render(request, 'maktablar.html', {"maktab":maktab})