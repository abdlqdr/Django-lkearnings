from django.shortcuts import render
from .models import ExamCenter, Student

# Create your views here.
def home(request):
    examcenter = ExamCenter.objects.all()
    student = Student.objects.all()
    print(examcenter)
    print(student)
    return render(request, 'school/home.html', {'centers':examcenter, 'students':student})