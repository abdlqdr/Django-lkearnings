from django.shortcuts import render
from .models import Teacher, Construction, Student
# Create your views here.

def home(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    constructor = Construction.objects.all()
    return render(request, 'school/home.html', {'students': student, 'teachers':teacher, 'constructors':constructor})