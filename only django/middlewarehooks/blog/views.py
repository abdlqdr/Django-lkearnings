from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print("I am a view")
    return HttpResponse("This is home page")

def exc(request):
    print("I am exception view")
    a = 10/0
    return HttpResponse("Excp page")

def user_info(request):
    print("I am user view")
    context = {'name': 'Rahul'}
    return TemplateResponse(request, 'blog/user.html', context)