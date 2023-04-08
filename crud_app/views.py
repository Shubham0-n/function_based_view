from django.shortcuts import render


def listview(request):
    return render(request, "crud.html")


def createview(request):
    return render(request, "crud.html")


def updateview(request):
    return render(request, "crud.html")


def deleteview(request):
    return render(request, "crud.html")
