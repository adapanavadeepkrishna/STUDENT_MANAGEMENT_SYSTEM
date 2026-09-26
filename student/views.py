from django.shortcuts import render
from .models import Student

def add_student(request):
    if request.method == 'POST':
        roll = request.POST['roll']
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            roll=roll,
            name=name,
            age=age,
            course=course
        )

    return render(request, 'add_student.html')

def view_student(request):
    students = Student.objects.all()
    return render(request, 'view_student.html', {'students': students})