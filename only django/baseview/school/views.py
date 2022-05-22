from re import L
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def myview(request):
    return HttpResponse('<h1> Function Based View </h1>')

class MyView(View):
    name = 'Abdul'
    def get(self, request):
        return HttpResponse(self.name)
        
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
    
def newsfun(request, template_name):
    template_name = template_name
    context = {'info':'cbi enquiry in this database'}
    return render(request, template_name, context)

class newsfunclass(View):
    template_name=''
    def get(self, request):
        context = {'info':'cbi enquiry in this database'}
        return render(request, self.template_name, context)