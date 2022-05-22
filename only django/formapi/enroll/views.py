from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration
from .models import user

# Create your views here.
def Student_form(request):
    if request.method == 'POST':
        fm= StudentRegistration()
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/student.html', {'form': fm})

def Teacher_form(request):
    if request.method == 'POST':
        fm= TeacherRegistration()
        if fm.is_valid():
            fm.save()
    else:
        fm = TeacherRegistration()
    return render(request, 'enroll/teacher.html', {'form': fm})