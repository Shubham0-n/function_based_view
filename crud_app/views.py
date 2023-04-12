from django.shortcuts import render, redirect, get_object_or_404
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


def updateview(request, pk):
    student = get_object_or_404(Student, id=pk)
    print(student)
    if request.method == "POST":
        form = StudentForms(request.POST, request.FILES, instance=student)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("crud:list-view")
    else:
        form = StudentForms(instance=student)
    students = Student.objects.all()
    context = {"form": form, "students": students, "id": pk}
    return render(request, "edit.html", context)


def deleteview(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return redirect("crud:list-view")
