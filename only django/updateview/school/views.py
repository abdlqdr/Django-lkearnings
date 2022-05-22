from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student
from django.views.generic.base import TemplateView
from django import forms
from .forms import StudentForm

# Create your views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    # model = Student
    # fields = ['name', 'email', 'password']
    success_url = '/thanks/'

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
    #     return form

class ThanksTemplateview(TemplateView):
    template_name = 'school/thanks.html'
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'

    # model = Student
    # fields = ['name', 'email', 'password']
    success_url = '/updated/'
    
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
    #     return form
    
class UpdateTemplateview(TemplateView):
    template_name = 'school/update.html'