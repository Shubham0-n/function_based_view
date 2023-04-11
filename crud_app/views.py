from django.shortcuts import render, redirect
from .forms import StudentForms
from .models import Student


def listview(request):
    students = Student.objects.all()
    context = {"form": StudentForms, "students": students}
    return render(request, "crud.html", context)


def createview(request):
    if request.method == "POST":
        form = StudentForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("crud:list-view")
    else:
        form = StudentForms()
    students = Student.objects.all()
    context = {"form": form, "students": students}
    return render(request, "crud.html", context)


def updateview(request):
    return render(request, "crud.html")


def deleteview(request):
    return render(request, "crud.html")
