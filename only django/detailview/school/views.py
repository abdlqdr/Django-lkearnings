from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class studentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'
    context_object_name = 'studen'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_student'] = self.model.objects.all().order_by('name')
        return context
    
class StudentListView(ListView):
    model = Student