from django.shortcuts import render
from .models import ExamCenter, MyExamCenter

# Create your views here.
def home(request):
    # examcenter = ExamCenter.objects.all()
    examcenter = MyExamCenter.abdul.quadir(102, 103)
    return render(request, 'school/home.html', {'myexamcenters': examcenter})