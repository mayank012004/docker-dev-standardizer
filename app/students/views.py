from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST["name"],
            roll_number=request.POST["roll_number"],
            department=request.POST["department"]
        )

    students = Student.objects.all()

    return render(request, "students/index.html", {
        "students": students
    })


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")


def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.roll_number = request.POST["roll_number"]
        student.department = request.POST["department"]
        student.save()
        return redirect("student_list")

    return render(request, "students/edit.html", {
        "student": student
    })