from django.shortcuts import render
from .forms import StudentForms


def listview(request):
    context = {"form": StudentForms}
    return render(request, "crud.html", context)


def createview(request):
    return render(request, "crud.html")


def updateview(request):
    return render(request, "crud.html")


def deleteview(request):
    return render(request, "crud.html")
