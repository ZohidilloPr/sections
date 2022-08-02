from django.shortcuts import render, redirect
from .models import People, Tuman
from .forms import PeopleForm
# Create your views here.

def Home(request):
    app = People.objects.all()
    return render(request, "home.html", {"app":app})

def Add_(request):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("HM")
    form = PeopleForm
    return render(request, 'add.html', context={
        "form":form
    })

def load_tuman(request):
    davlat_id = request.GET.get("davlat_id")
    tuman = Tuman.objects.filter(davlat_id=davlat_id).all()
    return render(request, 'tuman_dropdown.html', {"tuman":tuman})