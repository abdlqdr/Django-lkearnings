from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class studentListView(ListView):
    model = Student
    # template_name_suffix = '_set'
    # ordering = ['course']
    template_name = 'school/student.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        return Student.objects.filter(course='java')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context