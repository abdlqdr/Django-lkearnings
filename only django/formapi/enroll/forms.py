from django import forms
from django.forms import fields, widgets
from .models import user
from django.forms.fields import CharField

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = user
        fields = ['student_name', 'email', 'password']    

class TeacherRegistration(StudentRegistration):
    
    class Meta(StudentRegistration.Meta):
        model = user
        fields = ['teacher_name', 'email', 'password']    
    