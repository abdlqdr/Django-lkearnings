from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from django.views.generic.base import TemplateView
from .forms import StudentForm

# Create your views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/updated/'
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'school/studel.html'
    success_url = '/thanksdelete/'
    
class UpdateTemplateview(TemplateView):
    template_name = 'school/update.html'

class ThanksTemplateview(TemplateView):
    template_name = 'school/thanks.html'

class ThanksDeleteTemplateview(TemplateView):
    template_name = 'school/thanksdelete.html'